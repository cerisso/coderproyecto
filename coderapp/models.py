from django.db import models

# Create your models here.
class Curso(models.Model):
    
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField(primary_key=True)

class Estudiiante (models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.IntegerField()  
    email = models.EmailField()

class Profesor (models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.IntegerField()  
    email = models.EmailField() 
    profesion = models.CharField(max_length=60) 

class Entregable (models.Model):
    calificacion_minima = models.FloatField
    nombre = models.CharField(max_length=40)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()      