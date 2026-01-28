import os
import cloudinary
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_hv.settings')

# Configuración forzada con tus llaves activas
cloudinary.config( 
  cloud_name = "drhblvng5", 
  api_key = "945383893211668", 
  api_secret = os.environ.get('CLOUDINARY_API_SECRET'),
  secure = True
)

application = get_wsgi_application()