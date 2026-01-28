import os
import dj_database_url
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# --- SEGURIDAD ---
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-jover-moreira-2026-proyecto-final-hv')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://hoja-vida-36dy.onrender.com']

# --- APLICACIONES ---
INSTALLED_APPS = [
    'cloudinary_storage',
    'cloudinary',
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
    'whitenoise.middleware.WhiteNoiseMiddleware', # Vital para los estilos
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proyecto_hv.urls'

WSGI_APPLICATION = 'proyecto_hv.wsgi.application'

# --- BASE DE DATOS ---
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600
    )
}

# --- ESTÁTICOS Y CLOUDINARY ---
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_final')

# Configuración simplificada para evitar errores de archivos faltantes
STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'drhblvng5',
    'API_KEY': '945383893211668',
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
    'PREFIX': 'media'
}

# --- MANEJO DE MEMORIA PARA SUBIDAS ---
# Esto evita el Error 500 al guardar fotos en Render
FILE_UPLOAD_HANDLERS = [
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
]

MEDIA_URL = '/media/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'