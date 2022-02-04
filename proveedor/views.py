from django.shortcuts import redirect, render
from .models import Proveedor
from .forms import ProveeForm
# Create your views here.
def listarProveedores(request):
    proveedor=Proveedor.objects.all()
    return render(request,'proveedor/index.html',{"data":proveedor})

def crearProveedores(request):
    if request.method=="POST":
        form=ProveeForm(data=request.POST)
        if form.is_valid():
            provee=form.save(commit=False)
            provee.save() #se guarda en la db   

        return redirect('/proveedores')
    else:
        form=ProveeForm()
        #return render(request,'catalogo/reclamoejemplo.html',{"form":form})
        return render(request,'proveedor/nuevoProveedor.html',{"form":form})

