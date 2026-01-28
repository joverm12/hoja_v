import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_hv.settings')
django.setup()

from django.contrib.auth.models import User

# Cambia 'admin_nuevo' y 'tu_password_aqui' por lo que quieras
if not User.objects.filter(username='jover123').exists():
    User.objects.create_superuser('jover123', 'joverjesusmoreiramero@gmail.com', '123qwejover')
    print("Superusuario creado con éxito")
else:
    print("El usuario ya existe")