# Django Admin Theme Personalization

## Features
- Dynamic theme upload & activation
- SCSS compilation via Celery
- REST and GraphQL API support
- AI-driven color contrast validation

## Setup
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

## Run
```bash
celery -A admin_theme_project worker --loglevel=info
python manage.py runserver
```

## API
- `POST /api/themes/<id>/apply/`
- GraphQL mutation: `applyTheme(themeId: ID)`

## Notes
- Ensure Redis is running for Celery
- Override admin templates to reflect active themes
- Use `bleach` to sanitize CSS input
- Cache active theme for performance
#   a d m i n  
 