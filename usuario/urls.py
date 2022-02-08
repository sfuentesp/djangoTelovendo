from django import views
from django.urls import path
from . import views
urlpatterns=[
   
        path('', views.login, name="login-usu"),
        path('logout/', views.login, name="logout-usu"),
        path('bienvenido/', views.bienvenido),
    
    ]