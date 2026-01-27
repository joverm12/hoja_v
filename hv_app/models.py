from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

# Validador para asegurar que no se ingresen fechas del futuro
def validar_fecha_no_futura(value):
    if value > timezone.now().date():
        raise ValidationError('¡Cuidado! No puedes poner una fecha futura.')

# TABLA 1: DATOS PERSONALES
class DatosPersonales(models.Model):
    foto = models.ImageField(upload_to='perfil/', null=True, blank=True)
    sobre_mi = models.TextField(help_text="Escribe algo sobre ti (Acerca de mí)")
    apellidos = models.CharField(max_length=60)
    nombres = models.CharField(max_length=60)
    nacionalidad = models.CharField(max_length=20)
    lugarnacimiento = models.CharField(max_length=60)
    fechanacimiento = models.DateField(validators=[validar_fecha_no_futura])
    numerocedula = models.CharField(max_length=10, unique=True)
    sexo = models.CharField(max_length=1, choices=[('H', 'Hombre'), ('M', 'Mujer')])
    estadocivil = models.CharField(max_length=50)
    licenciaconducir = models.CharField(max_length=6, blank=True)
    telefonoconvencional = models.CharField(max_length=15, blank=True)
    telefonofijo = models.CharField(max_length=15)
    direcciontrabajo = models.CharField(max_length=100, blank=True)
    direcciondomiciliaria = models.CharField(max_length=100)
    sitioweb = models.URLField(max_length=100, blank=True)
    universidad = models.CharField(max_length=100, default="Universidad Laica Eloy Alfaro de Manabí")
    carrera = models.CharField(max_length=100, default="Tecnología de la Información")
    periodo_u = models.CharField(max_length=50, default="Mayo 2024 - En curso")
    bachillerato_status = models.CharField(max_length=100, default="Bachillerato - Completo")
    certificado_bachiller_pdf = models.FileField(upload_to='certificados/', null=True, blank=True)
    aptitudes = models.TextField(help_text="Separa tus habilidades por comas")

    def __str__(self): return f"{self.nombres} {self.apellidos}"

# TABLA 2: EXPERIENCIA LABORAL
class ExperienciaLaboral(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    cargodesempenado = models.CharField(max_length=100)
    nombrempresa = models.CharField(max_length=100)
    fechainicio = models.DateField(validators=[validar_fecha_no_futura])
    fechafin = models.DateField(null=True, blank=True, validators=[validar_fecha_no_futura])
    actividadesrealizadas = models.TextField()
    activarparaqueseveaenfront = models.BooleanField(default=True)

# TABLA 3: RECONOCIMIENTO
class Reconocimiento(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    nombrereconocimiento = models.CharField(max_length=100)
    institucionqueotorga = models.CharField(max_length=100)
    fechareconocimiento = models.DateField(validators=[validar_fecha_no_futura])
    descripcion = models.TextField(blank=True, null=True, help_text="Se mostrará si no hay archivo adjunto")
    comprobante_archivo = models.FileField(upload_to='reconocimientos/', null=True, blank=True)
    activarparaqueseveaenfront = models.BooleanField(default=True)

# TABLA 4: CURSO REALIZADO
class CursoRealizado(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    nombrecurso = models.CharField(max_length=150)
    nombreinstitucion = models.CharField(max_length=100)
    numerohoras = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True, help_text="Escribe qué aprendiste si no tienes el certificado PDF")
    certificado_pdf = models.FileField(upload_to='cursos/', null=True, blank=True)
    activarparaqueseveaenfront = models.BooleanField(default=True)

# TABLA 5: PRODUCTO ACADÉMICO
class ProductoAcademico(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    nombrerecurso = models.CharField(max_length=100)
    clasificador = models.CharField(max_length=100)
    descripcion = models.TextField()
    activarparaqueseveaenfront = models.BooleanField(default=True)

# TABLA 6: PRODUCTO LABORAL
class ProductoLaboral(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    nombreproducto = models.CharField(max_length=100)
    fechaproducto = models.DateField(validators=[validar_fecha_no_futura])
    descripcion = models.TextField(blank=True, null=True, help_text="Describe el producto laboral")
    activarparaqueseveaenfront = models.BooleanField(default=True)

# TABLA 7: VENTA GARAGE (Con campo descripción agregado)
class VentaGarage(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    nombreproducto = models.CharField(max_length=100)
    estadoproducto = models.CharField(max_length=40)
    valordelbien = models.DecimalField(max_digits=10, decimal_places=2)
    # NUEVO CAMPO:
    descripcion = models.TextField(blank=True, null=True, help_text="Detalles del artículo")
    foto_producto = models.ImageField(upload_to='garage/', null=True, blank=True)
    activarparaqueseveaenfront = models.BooleanField(default=True)