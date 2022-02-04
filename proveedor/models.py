from django.db import models
from django.forms import CharField

# Create your models here.

class Proveedor(models.Model):
    rut=models.CharField(max_length=12,null=False)
    nombre=models.CharField(max_length=50,null=False)
    dire=models.CharField(max_length=200)
    telefono=models.IntegerField()
    
    
    
    