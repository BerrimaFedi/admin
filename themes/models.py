# themes/models.py
from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re

COLOR_REGEX = r'^#(?:[0-9a-fA-F]{3}){1,2}$'

def validate_asset_url(value):
    if not value.startswith("https://"):
        raise ValidationError("URL must use HTTPS.")
    if not re.search(r'\.(css|js)$', value):
        raise ValidationError("URL must end with .css or .js")

class AdminTheme(models.Model):
    name = models.CharField(max_length=100, unique=True)
    css_url = models.URLField(validators=[validate_asset_url])
    js_url = models.URLField(validators=[validate_asset_url], blank=True, null=True)
    primary_color = models.CharField(max_length=7, validators=[RegexValidator(regex=COLOR_REGEX)])
    secondary_color = models.CharField(max_length=7, validators=[RegexValidator(regex=COLOR_REGEX)])
    sidebar_position = models.CharField(choices=[("left", "Left"), ("right", "Right")], default="left", max_length=10)
    scss_variables = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
