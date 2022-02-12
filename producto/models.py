from django.db import models

# Create your models here.


class Producto(models.Model):
    sku=models.CharField(max_length=10,null=False)
    nombre=models.CharField(max_length=50,null=False)
    proveedor=models.CharField(max_length=50,null=False)
    cantidad=models.IntegerField()
    precio=models.IntegerField()
    