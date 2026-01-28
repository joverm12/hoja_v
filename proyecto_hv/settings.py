import os
import dj_database_url
from pathlib import Path

# --- CONFIGURACIÓN BÁSICA ---
BASE_DIR = Path(__file__).resolve().parent.parent

# SEGURIDAD: Lee la clave real de Render o usa la de respaldo si estás en local
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-jover-moreira-2026-proyecto-final-hv') #

DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['*']

# --- APLICACIONES ---
INSTALLED_APPS = [
    'cloudinary_storage', #
    'cloudinary',        #
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hv_app',
]

# --- MIDDLEWARE ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', #
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proyecto_hv.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            'django.template.context_processors.media', #
        ],
    },
}]

WSGI_APPLICATION = 'proyecto_hv.wsgi.application'

# --- BASE DE DATOS ---
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600
    )
}

# --- INTERNACIONALIZACIÓN ---
LANGUAGE_CODE = 'es-ec'
TIME_ZONE = 'America/Guayaquil'
USE_I18N = True
USE_TZ = True

# --- ARCHIVOS ESTÁTICOS Y ALMACENAMIENTO ---
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_final')

# SOLUCIÓN DJANGO 6.0 + WHITE NOISE + CLOUDINARY
STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# Líneas de compatibilidad para evitar el AttributeError en Render
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# --- CREDENCIALES DE CLOUDINARY ---
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'drhblvng5',
    'API_KEY': '945383893211668',
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'), #
}

MEDIA_URL = '/media/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- LÍMITES DE SUBIDA ---
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 10MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760