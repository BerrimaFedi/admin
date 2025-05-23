# themes/urls.py

from django.urls import path
from .views import apply_theme

urlpatterns = [
    path('themes/<int:pk>/apply/', apply_theme, name='apply-theme'),
]
