import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_hv.settings')
django.setup()

from django.contrib.auth.models import User

# Cambia estos datos por los que tú quieras
username = 'tu_nombre'
email = 'tu@email.com'
password = 'tu_contraseña_segura'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"Superusuario {username} creado con éxito")
else:
    print("El usuario ya existe")