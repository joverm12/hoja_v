from django.shortcuts import render
from .models import *

def home(request):
    perfil = DatosPersonales.objects.first()
    context = {
        'p': perfil,
        'skills': perfil.aptitudes.split(',') if perfil and perfil.aptitudes else [],
        'experiencias': ExperienciaLaboral.objects.filter(activarparaqueseveaenfront=True),
        'reconocimientos': Reconocimiento.objects.filter(activarparaqueseveaenfront=True),
        'cursos': CursoRealizado.objects.filter(activarparaqueseveaenfront=True),
        'academicos': ProductoAcademico.objects.filter(activarparaqueseveaenfront=True),
        'laborales': ProductoLaboral.objects.filter(activarparaqueseveaenfront=True),
        'garage': VentaGarage.objects.filter(activarparaqueseveaenfront=True),
    }
    return render(request, 'index.html', context)