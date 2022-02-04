from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'producto/index.html')

def listadoProductos(request):
    productos={

        "Productos":[{

            "ID":1,
            "Nombre":"Platano",
            "Valor":1000,
            "Stock":20

        },
        {

            "ID":2,
            "Nombre":"Pera",
            "Valor":1200,
            "Stock":10

        }
        ]

    }
    return render(request,'producto/listadoProductos.html',productos)