import email
from tkinter import CASCADE
from django.db import models
from django.forms import CharField


# Create your models here.

class Proveedor(models.Model):
    rut=models.CharField(max_length=12,null=False)
    nombre=models.CharField(max_length=50,null=False)
    dire=models.CharField(max_length=200)
    telefono=models.IntegerField()
    email=models.EmailField()
    username=models.CharField(max_length=8)
    password=models.CharField(max_length=8)
    
    

    
    
    

    
    
    
    