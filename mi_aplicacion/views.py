from django.shortcuts import render
from .models import Actividad

def lista_actividades(request):
    actividades = Actividad.objects.all()
    return render(request, 'mi_aplicacion/lista_actividades.html', {'actividades': actividades})