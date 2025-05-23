from django.core.cache import cache
from .models import AdminTheme

def active_theme(request):
    theme = cache.get('active_theme')
    if not theme:
        theme = AdminTheme.objects.filter(is_active=True).first()
        cache.set('active_theme', theme, 60 * 60)
    return {'active_theme': theme}
