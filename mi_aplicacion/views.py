from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Actividad
from .forms import ActividadForm

def lista_actividades(request):
    """Vista principal que muestra todas las actividades"""
    actividades = Actividad.objects.all().order_by('-fecha_creacion')
    
    # Calcular estadísticas
    total = actividades.count()
    completadas = actividades.filter(completada=True).count()
    pendientes = actividades.filter(completada=False).count()
    
    context = {
        'actividades': actividades,
        'total': total,
        'completadas': completadas,
        'pendientes': pendientes,
    }
    
    return render(request, 'mi_aplicacion/lista_actividades.html', context)

def detalle_actividad(request, pk):
    """Vista que muestra el detalle de una actividad específica"""
    actividad = get_object_or_404(Actividad, pk=pk)
    return render(request, 'mi_aplicacion/detalle_actividad.html', {'actividad': actividad})

def crear_actividad(request):
    """Vista para crear una nueva actividad"""
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Actividad creada exitosamente!')
            return redirect('lista_actividades')
    else:
        form = ActividadForm()
    return render(request, 'mi_aplicacion/form_actividad.html', {'form': form, 'titulo': 'Nueva Actividad'})

def editar_actividad(request, pk):
    """Vista para editar una actividad existente"""
    actividad = get_object_or_404(Actividad, pk=pk)
    if request.method == 'POST':
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Actividad actualizada exitosamente!')
            return redirect('detalle_actividad', pk=pk)
    else:
        form = ActividadForm(instance=actividad)
    return render(request, 'mi_aplicacion/form_actividad.html', {'form': form, 'titulo': 'Editar Actividad', 'actividad': actividad})

def eliminar_actividad(request, pk):
    """Vista para eliminar una actividad"""
    actividad = get_object_or_404(Actividad, pk=pk)
    if request.method == 'POST':
        actividad.delete()
        messages.success(request, '¡Actividad eliminada exitosamente!')
        return redirect('lista_actividades')
    return render(request, 'mi_aplicacion/confirmar_eliminacion.html', {'actividad': actividad})

def toggle_completada(request, pk):
    """Vista para marcar/desmarcar una actividad como completada"""
    actividad = get_object_or_404(Actividad, pk=pk)
    actividad.completada = not actividad.completada
    actividad.save()
    estado = "completada" if actividad.completada else "pendiente"
    messages.success(request, f'¡Actividad marcada como {estado}!')
    return redirect('lista_actividades')