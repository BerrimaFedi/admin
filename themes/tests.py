# themes/tests.py
import pytest
from django.core.exceptions import ValidationError
from .models import AdminTheme

@pytest.mark.django_db
def test_invalid_color():
    with pytest.raises(ValidationError):
        AdminTheme(primary_color='notacolor').full_clean()
