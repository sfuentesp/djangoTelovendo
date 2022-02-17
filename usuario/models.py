
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Usuario(models.Model):
    rut=models.CharField(max_length=10)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    comentario = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk} )