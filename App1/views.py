from django.shortcuts import render
from App1.models import *
from django.http import HttpResponse
from App1.forms import Formulario1


def inicio(request):
    return render(request, "App1/inicio.html")


def Usuario(request):
    
    return render(request, "App1/usuario.html")

def Rango(request):
    
    return render(request, "App1/rangos.html")

def FechaDeCreacion(request):
    
    return render(request, "App1/fechas.html")

def formulario(request):
    if request.method == "POST":

        f1= Formulario1(request.POST)
        if f1.is_valid():

            info = f1.cleaned_data

            nick = nickname(nombre=info["nombre"], contraseña=info["contraseña"])
            level = rango(nivel=info["nivel"], liga=info["liga"])
            create = fechadecreacion(fecha=info["fecha"])
            create.save()
            level.save()
            nick.save()
            return render(request, "App1/inicio.html")
        
    else:
        f1=Formulario1()
            

    return render(request, "App1/Formulario.html", {"form1":f1})

def buscarnickname(request):
    return render(request, "App1/buscarnick.html")

def resultado(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        nicks= nickname.objects.filter(nombre__icontains=nombre)

        return render(request, "App1/resultados.html",{"nicks":nicks, "nombre":nombre})
    else:
        respuesta = "No enviaste datos"


    return HttpResponse(respuesta)