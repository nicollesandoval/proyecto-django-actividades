from django import forms
from .models import Actividad

class ActividadForm(forms.ModelForm):
    """Formulario para crear y editar actividades"""
    
    class Meta:
        model = Actividad
        fields = ['titulo', 'descripcion', 'completada']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Completar informe mensual',
                'maxlength': '200'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe los detalles de tu actividad...',
                'rows': 5
            }),
            'completada': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
        labels = {
            'titulo': 'Título de la actividad',
            'descripcion': 'Descripción',
            'completada': '¿Actividad completada?'
        }
        help_texts = {
            'titulo': 'Máximo 200 caracteres',
            'descripcion': 'Proporciona una descripción detallada de la actividad'
        }
