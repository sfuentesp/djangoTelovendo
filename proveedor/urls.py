from django.urls import path
from . import views

urlpatterns=[
   
        path('', views.listarProveedores),
        path('nuevoProveedor/', views.crearProveedores, name="Agregar-Provee"),
    
    ]