import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise # <--- ESTO ES VITAL

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_hv.settings')

# 1. Iniciamos la aplicación normal
application = get_wsgi_application()

# 2. La envolvemos con WhiteNoise para que Render encuentre los estilos y el JS del formulario
# Esto elimina el error "No hay directorio en: /static_final/"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'static_final'))