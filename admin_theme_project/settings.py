# admin_theme_project/settings.py
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'themes',                  
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'graphene_django',
    'admin_theme_project',
]


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

GRAPHENE = {
    'SCHEMA': 'themes.schema.schema',
}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'admin-theme',        
        'USER': 'postgres', 
        'PASSWORD': 'root',  
        'HOST': 'localhost',
        'PORT': '5432',               
    }
}

CELERY_BROKER_URL = 'redis://localhost:6379/0'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # your custom templates folder
        'APP_DIRS': True,                  # <---- Add this line
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
DEBUG = True  # ← obligatoire sinon ALLOWED_HOSTS est exigé

ALLOWED_HOSTS = ['*']
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
ROOT_URLCONF = 'admin_theme_project.urls'
SECRET_KEY = '+dfpx^(+5zfw$t=x=hgeuccholy0z1tk5%tcxlm10@110i5&+0'
