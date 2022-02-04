from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name="producto-home"),
    path('listado/', views.listadoProductos, name="producto-listado Productos")
    
    ]