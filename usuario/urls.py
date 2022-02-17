from django import views
from django.urls import path
from .views import PostCreateView,PostDetailView,PostListViews,PostUpdateView,PostDeleteView
from . import views
urlpatterns=[
   
        path('login/', views.login, name="login"),
        path('logout/', views.salir, name="logout-usu"),
        path('bienvenido/', views.bienvenido),
        path('crearusuarioDjango/',views.crearUsuario,name="crear-usu-django"),
        path('crearusuarioApps/',views.agregarUsuario,name="crear-usu-apps"),
        path('usuarios/listado',views.listarUser,name="crear-usu"),

        path('post', PostListViews.as_view(), name = 'post-list' ),
        path('post/nuevo', PostCreateView.as_view(), name = 'post-create' ),
        path('post/<int:pk>', PostDetailView.as_view(), name = 'post-detail' ),
        path('post/<int:pk>/update', PostUpdateView.as_view(), name = 'post-update'),
        path('post/<int:pk>/delete', PostDeleteView.as_view(), name = 'post-delete'),
    ]