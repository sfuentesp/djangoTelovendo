from django import views
from django.urls import path
from . import views
urlpatterns=[
   
        path('login/', views.login, name="login"),
        path('logout/', views.salir, name="logout-usu"),
        path('bienvenido/', views.bienvenido),
        path('crearusuario/',views.crearUsuario),
    
    ]