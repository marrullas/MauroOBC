from django.db import models

# Create your models here.

class Director(models.Model):
    nombre = models.CharField(max_length=60)
    web =  models.CharField(max_length=64, null=True)
    bio = models.TextField(max_length=400, null=True, help_text="Escribir biografia")

    def __str__(self):
        return (self.nombre)

class Pelicula(models.Model):
    nombre= models.CharField(max_length=100)
    director= models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    sumario = models.TextField(max_length=250, help_text="Colocar el resumen de la peli", null=True)
