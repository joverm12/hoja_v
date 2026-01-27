from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import *

# Limpieza del panel
admin.site.unregister(User)
admin.site.unregister(Group)

# 1. Especial para Datos Personales: Quita el botón "+" si ya existe tu perfil
class DatosPersonalesAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Si ya hay un registro, devuelve False para ocultar el botón "Añadir"
        if DatosPersonales.objects.exists():
            return False
        return True

# 2. Clase para auto-asignar tu perfil en las otras secciones
class MiHojaDeVidaAdmin(admin.ModelAdmin):
    exclude = ('perfil',) # Oculta el desplegable

    def save_model(self, request, obj, form, change):
        mi_perfil = DatosPersonales.objects.first()
        if mi_perfil:
            obj.perfil = mi_perfil
        super().save_model(request, obj, form, change)

# Registro con las nuevas reglas
admin.site.register(DatosPersonales, DatosPersonalesAdmin) # Usa la regla de no añadir más
admin.site.register(ExperienciaLaboral, MiHojaDeVidaAdmin)
admin.site.register(Reconocimiento, MiHojaDeVidaAdmin)
admin.site.register(CursoRealizado, MiHojaDeVidaAdmin)
admin.site.register(ProductoAcademico, MiHojaDeVidaAdmin)
admin.site.register(ProductoLaboral, MiHojaDeVidaAdmin)
admin.site.register(VentaGarage, MiHojaDeVidaAdmin)