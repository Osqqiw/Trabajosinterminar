from django.db import models

class Curso(models.Model):
    nombre = models.CharField(verbose_name="Nombre del curso", max_length=50)
    duracion = models.CharField(verbose_name="Duracion", max_length=50) #Ejemplo: "24 clases"
    datos = models.CharField(verbose_name="Nombre y Apellido del profesor", max_length=50)

    def __str__(self):
        return self.nombre 

class Alumnos(models.Model):
    nombre_alumno = models.CharField(verbose_name="Nombre del curso", max_length=50)
    apellido = models.CharField(verbose_name="Apellido", max_length=50)
    documento = models.CharField(verbose_name="Numero de documento", max_length=50)
    email  = models.CharField(verbose_name="Correo electronico", max_length=50)
    def __str__(self):
        return self.nombre_alumno
    
class Trabajos_Practicos(models.Model):
    fecha_de_entrega = models.DateField()
    asignatura = models.CharField(verbose_name="Asignatura", max_length=50)
    def __str__(self):
        return self.asignatura
