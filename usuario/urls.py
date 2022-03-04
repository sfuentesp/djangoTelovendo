from django import views
from django.urls import path
from .views import ProveedorListViews, SubCategoriaCreateView,CategoriaCreateView, PostCreateView,PostDetailView,PostListViews,PostUpdateView,PostDeleteView, ProveedorCreateView
from . import views
urlpatterns=[
   
        path('login/', views.login, name="login"),
        path('logout/', views.salir, name="logout-usu"),
        path('bienvenido/', views.bienvenido),
        path('crearusuarioDjango/',views.crearUsuario,name="crear-usu-django"),
     
        path('usuarios/listado',views.listarUser,name="usuarios-listado"),

        path('post', PostListViews.as_view(), name = 'post-list' ),
        path('post/nuevo', PostCreateView.as_view(), name = 'post-create' ),
        path('post/<int:pk>', PostDetailView.as_view(), name = 'post-detail' ),
        path('post/<int:pk>/update', PostUpdateView.as_view(), name = 'post-update'),
        path('post/<int:pk>/delete', PostDeleteView.as_view(), name = 'post-delete'),

        
        path('proveedor', ProveedorListViews.as_view(), name = 'proveedor-listado' ),
        path('proveedor/nuevo', ProveedorCreateView.as_view(), name = 'proveedor-create' ),
        
        path('categoria', CategoriaCreateView.as_view(), name = 'categoria-create' ),
        
        path('subcategoria', SubCategoriaCreateView.as_view(), name = 'subcategoria-create' ),

    ]