import email
from django.shortcuts import redirect, render
from .forms import LoginForm, UserForm, FormUsuario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required

from .models import Usuario
# Create your views here.



#creacion de usuario de la app
def agregarUsuario(request):
    form=FormUsuario()
    if request.method=="POST":
        form=FormUsuario(data=request.POST)
        usu=form.save(commit=False)#aqui los valore estan en memoria
        usu.save()
        
        return redirect('/usuarios/listado')
    else:
        
        return render(request,'usuario/createUsuario.html',{"form":form})

#creacion de usuario django
def crearUsuario(request):
    if request.method=="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            nombre=form.cleaned_data["nombre"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            user= User.objects.create_user(nombre,email,password)
            user.save()
        return redirect("/crearusuario")

    else:
        form=UserForm()
        return render(request, 'usuario/createuser.html',{'form':form})

def listarUser(request):
    usu=Usuario.objects.all()
    usu2=User.objects.all()
    return render(request,'usuario/listarUsuarios.html',{"usu":usu,"usu2":usu2})

def login(request):
    if request.method=="POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            
            usu=form.cleaned_data["nombre"]
            clave=form.cleaned_data["password"]
            user=authenticate(request,username=usu,password=clave)
           
            if user is not None:
                auth_login(request,user)
                return render(request,'usuario/bienvenida.html',{"user":user})
            else:
                return redirect("/login")
           
    else:
        form=LoginForm()
        return render(request,'usuario/login.html',{"form":form})

@login_required(login_url="/login")
def bienvenido(request):
    return render(request,'usuario/bienvenida.html')

def salir(request):
    logout(request)
    return redirect("/login")