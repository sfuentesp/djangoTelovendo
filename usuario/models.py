from django.db import models

# Create your models here.


class Usuario(models.Model):
    rut=models.CharField(max_length=10)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    