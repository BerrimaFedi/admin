from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .models import AdminTheme
from .tasks import compile_scss
from django.core.cache import cache

@api_view(['POST'])
@permission_classes([IsAdminUser])
def apply_theme(request, pk):
    theme = get_object_or_404(AdminTheme, pk=pk)
    AdminTheme.objects.update(is_active=False)
    theme.is_active = True
    theme.save()

    cache.set('active_theme', theme, 60 * 60)
    compile_scss.delay(theme.id)

    return Response({'status': 'Theme applied', 'theme': theme.name})
