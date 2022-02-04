from http import client
from django.shortcuts import render


def home(request):
    return render(request,'cliente/index.html')

def listadoClientes(request):
    
    clie={

        "Clientes":[{

            "ID":1,
            "Nombre":"Juan",
            "Edad":21
           
        },
        {

            "ID":2,
            "Nombre":"Pedro",
            "Edad":22
         
        },
        {

            "ID":3,
            "Nombre":"Diego",
            "Edad":50
         
        },
        {

            "ID":4,
            "Nombre":"Ramon",
            "Edad":34
         
        },
        {

            "ID":5,
            "Nombre":"Mario",
            "Edad":60
         
        }
        ]

    }

  
    return render(request,'cliente/index.html',clie)