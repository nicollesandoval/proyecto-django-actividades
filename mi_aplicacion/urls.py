from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_actividades, name='lista_actividades'),
    path('actividad/<int:pk>/', views.detalle_actividad, name='detalle_actividad'),
    path('actividad/nueva/', views.crear_actividad, name='crear_actividad'),
    path('actividad/<int:pk>/editar/', views.editar_actividad, name='editar_actividad'),
    path('actividad/<int:pk>/eliminar/', views.eliminar_actividad, name='eliminar_actividad'),
    path('actividad/<int:pk>/toggle/', views.toggle_completada, name='toggle_completada'),
]