from django import views
from django.urls import path
from . import views
urlpatterns=[
   
        path('login/', views.login, name="login"),
        path('logout/', views.salir, name="logout-usu"),
        path('bienvenido/', views.bienvenido),
        path('crearusuarioDjango/',views.crearUsuario,name="crear-usu-django"),
        path('crearusuarioApps/',views.agregarUsuario,name="crear-usu-apps"),
        path('usuarios/listado',views.listarUser,name="crear-usu"),
    
    ]