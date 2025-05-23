from django import forms
from .models import AdminTheme

class AdminThemeForm(forms.ModelForm):
    class Meta:
        model = AdminTheme
        fields = '__all__'
        widgets = {
            'scss_variables': forms.Textarea(attrs={'rows': 6}),
            'primary_color': forms.TextInput(attrs={'type': 'color'}),
            'secondary_color': forms.TextInput(attrs={'type': 'color'}),
        }
