from django.urls import path
from .views import apply_theme

urlpatterns = [
    path('<int:pk>/apply/', apply_theme, name='apply-theme'),
]
