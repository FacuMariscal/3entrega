from django.shortcuts import render
from App1.models import *
from django.http import HttpResponse
from App1.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin



def iniciosesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data =request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            clave = form.cleaned_data.get("password")

            user = authenticate(username = usuario, password = clave)

            if user:
                login(request, user)
                
                return render(request, "App1/inicio.html",{"mensaje":f"Bienvenido{user}"})
        else:
            return render(request, "App1/inicio.html",{"mensaje":"Datos Incorrectos"})
    else:
        form = AuthenticationForm()
    
    return render(request, "App1/login.html",{"formulario":form})

def registro(request):
    if request.method == "POST":
        form = registrarse(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "App1/inicio.html",{"mensaje":"Usuario creado"})
    else:
        form = registrarse()
    return render(request,"App1/registro.html",{"formulario":form})






def inicio(request):
    return render(request, "App1/inicio.html")


def Personaje(request):
    return render(request, "App1/personajes.html")



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

class ListaPersonaje(LoginRequiredMixin, ListView):
    model = personaje

class DetallePersonaje(LoginRequiredMixin, DetailView):
    model = personaje

class CrearPersonaje(LoginRequiredMixin, CreateView):
    model = personaje
    success_url= "/App1/Personaje/list"
    fields = ["name","fuerza","velocidad","resistencia","tipo"]  

class ActualizarPersonaje(LoginRequiredMixin, UpdateView):
    model = personaje
    success_url= "/App1/Personaje/list"
    fields = ["name","fuerza","velocidad","resistencia","tipo"]     

class BorrarPersonaje(LoginRequiredMixin, DeleteView):
    model = personaje
    success_url= "/App1/Personaje/list"
    fields = ["name","fuerza","velocidad","resistencia","tipo"] 

class ListaUsuario(LoginRequiredMixin, ListView):
    model = usuario

class DetalleUsuario(LoginRequiredMixin, DetailView):
    model = usuario

class CrearUsuario(LoginRequiredMixin, CreateView):
    model = usuario
    success_url= "/App1/Usuario/list"
    fields = ["nombre","apellido","nivel","liga","fecha","email","imagen"]  

class ActualizarUsuario(LoginRequiredMixin, UpdateView):
    model = usuario
    success_url= "/App1/Usuario/list"
    fields = ["nombre","apellido","nivel","liga","fecha","email","imagen"]  
    

class BorrarUsuario(LoginRequiredMixin, DeleteView):
    model = usuario
    success_url= "/App1/Usuario/list"
    fields = ["nombre","apellido","nivel","liga","fecha","email","imagen"]  
