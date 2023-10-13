from django.shortcuts import render
from App1.models import *
from django.http import HttpResponse
from App1.forms import *


def inicio(request):
    return render(request, "App1/inicio.html")


def Personaje(request):
    return render(request, "App1/personajes.html")

def Usuario(request):
    
    return render(request, "App1/usuario.html")

def formulario(request):
    if request.method == "POST":

        f1= Formulario1(request.POST)
        if f1.is_valid():

            info = f1.cleaned_data

            nick = usuario(nombre=info["nombre"], contraseña=info["contraseña"],fecha=info["fecha"],nivel=info["nivel"], liga=info["liga"], email=info["email"])
            nick.save()
            return render(request, "App1/inicio.html")
        
    else:
        f1=Formulario1()
            

    return render(request, "App1/Formulario.html", {"form1":f1})

def formulario2(request):
    if request.method == "POST":
        f2= Formulario2(request.POST)
        if f2.is_valid():

            info = f2.cleaned_data
            pj = personaje(name=info["name"],fuerza=info["fuerza"],velocidad=info["velocidad"],resistencia=info["resistencia"],tipo=info["tipo"])
            pj.save()
            return render(request, "App1/inicio.html")
    else:
        f2=Formulario2()
    return render(request, "App1/Formulario2.html", {"form2":f2})



def buscarnickname(request):
    return render(request, "App1/buscarnick.html")

def resultado(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        nicks= usuario.objects.filter(nombre__icontains=nombre)

        return render(request, "App1/resultados.html",{"nicks":nicks, "nombre":nombre})
    else:
        respuesta = "No enviaste datos"


    return HttpResponse(respuesta)