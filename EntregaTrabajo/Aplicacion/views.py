from django.shortcuts import render, redirect
from .models import Curso, Alumnos, Trabajos_Practicos
from .forms import CursoForm, AlumnoForm, TrabajoPracticoForm

def inicio(request):
    return render(request, 'aplicacion.html')

def bienvenido(request):
    return render(request, 'aplicacion/bienvenido.html')

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'aplicacion/listar_cursos.html', {'cursos': cursos})

def nuevo_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()
    return render(request, 'aplicacion/nuevo_curso.html', {'form': form})

def listar_alumnos(request):
    alumnos = Alumnos.objects.all()
    return render(request, 'aplicacion/listar_alumnos.html', {'alumnos': alumnos})

def nuevo_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nuevo_alumno')
    else:
        form = AlumnoForm()
    return render(request, 'aplicacion/nuevo_alumno.html', {'form': form})

def listar_trabajos_practicos(request):
    trabajos_practicos = Trabajos_Practicos.objects.all()
    return render(request, 'aplicacion/listar_trabajos_practicos.html', {'trabajos_practicos': trabajos_practicos})

def nuevo_trabajo_practico(request):
    if request.method == 'POST':
        form = TrabajoPracticoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_trabajos_practicos')
    else:
        form = TrabajoPracticoForm()
    return render(request, 'aplicacion/nuevo_trabajo_practico.html', {'form': form})
