# themes/views.py
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .models import AdminTheme

@api_view(['POST'])
@permission_classes([IsAdminUser])
def apply_theme(request, pk):
    theme = get_object_or_404(AdminTheme, pk=pk)
    AdminTheme.objects.update(is_active=False)
    theme.is_active = True
    theme.save()
    return Response({'status': 'Theme applied', 'theme': theme.name})
