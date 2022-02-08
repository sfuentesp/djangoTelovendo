import email
from django.shortcuts import redirect, render
from .forms import LoginForm, ProveeFormLogin

from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


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
        form=LoginForm()
        return render(request,'usuario/login.html',{"form":form})

@login_required(login_url="/login")
def bienvenido(request):
    return render(request,'usuario/bienvenida.html')

def salir(request):
    logout(request)
    return redirect("login/")