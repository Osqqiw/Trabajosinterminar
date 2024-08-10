from django import forms
from .models import Curso, Alumnos, Trabajos_Practicos

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'duracion', 'datos']

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ['nombre_alumno', 'apellido', 'documento','email']

class TrabajoPracticoForm(forms.ModelForm):
    class Meta:
        model = Trabajos_Practicos
        fields = ['asignatura', 'fecha_de_entrega']
