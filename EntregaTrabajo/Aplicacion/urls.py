from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('bienvenido/', views.bienvenido, name='bienvenido'),
    path('cursos/', views.listar_cursos, name='listar_cursos'),
    path('nuevo_curso/', views.nuevo_curso, name='nuevo_curso'),
    path('alumnos/', views.listar_alumnos, name='listar_alumnos'),
    path('nuevo_alumno/', views.nuevo_alumno, name='nuevo_alumno'),
    path('trabajos_practicos/', views.listar_trabajos_practicos, name='listar_trabajos_practicos'),
    path('nuevo_trabajo_practico/', views.nuevo_trabajo_practico, name='nuevo_trabajo_practico'),
 ]
