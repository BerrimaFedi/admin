import sass  
import os
from celery import shared_task
from django.conf import settings
from .models import AdminTheme

@shared_task
def compile_scss(theme_id):
    theme = AdminTheme.objects.get(id=theme_id)

    out_path = os.path.join(settings.STATICFILES_DIRS[0], 'admin/themes', f"{theme.name}.css")

    try:
        compiled = sass.compile(string=theme.scss_variables)

        with open(out_path, 'w') as f:
            f.write(compiled)

        return {"status": "success"}

    except Exception as e:
        theme.is_active = False
        theme.save()
        return {"status": "error", "message": str(e)}
