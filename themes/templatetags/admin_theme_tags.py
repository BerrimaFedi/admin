from django import template
from themes.models import AdminTheme

register = template.Library()

@register.simple_tag
def get_active_admin_theme():
    return AdminTheme.objects.filter(is_active=True).first()
