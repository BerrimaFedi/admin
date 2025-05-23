from django.contrib import admin
from .models import AdminTheme
from django.utils.html import format_html
from .forms import AdminThemeForm



@admin.register(AdminTheme)
class AdminThemeAdmin(admin.ModelAdmin):
    form = AdminThemeForm
    list_display = ('name', 'is_active', 'primary_color_display', 'secondary_color_display', 'sidebar_position')
    list_filter = ('is_active', 'sidebar_position')
    search_fields = ('name',)
    ordering = ('name',)
    list_editable = ('is_active',)

    fieldsets = (
        (None, {
            'fields': ('name', 'css_url', 'js_url', 'is_active')
        }),
        ('Colors', {
            'fields': ('primary_color', 'secondary_color')
        }),
        ('Layout and Variables', {
            'fields': ('sidebar_position', 'scss_variables')
        }),
    )

    def primary_color_display(self, obj):
        return format_html(
            '<span style="color:{};">{}</span>',
            obj.primary_color,
            obj.primary_color
        )
    primary_color_display.short_description = 'Primary Color'

    def secondary_color_display(self, obj):
        return format_html(
            '<span style="color:{};">{}</span>',
            obj.secondary_color,
            obj.secondary_color
        )
    secondary_color_display.short_description = 'Secondary Color'
