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
from django.contrib.auth.decorators import login_required



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

@login_required
def editarUsuario(request):
    usuario = request.user

    if request.method == "POST":
        form = FormularioEditar(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.set_password = info["password1"]
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]

            usuario.save()

            return render(request, "App1/inicio.html")
    
    else:

        form = FormularioEditar(initial={"email":usuario.email,"first_name":usuario.first_name,"last_name":usuario.last_name,
        })
    
    return render(request, "App1/EditarPerfil.html",{"formulario":form, "usuario":usuario})



@login_required
def agregarAvatar(request):
    if request.method=="POST":

        form= AvatarFormulario(request.POST, request.FILES)

        if form.is_valid():
            usuarioActual = User.objects.get(username=request.user)
            Avatar = avatar(usuario= usuarioActual, imagen= form.cleaned_data["imagen"])

            Avatar.save()

            return render(request, "App1/inicio.html")
        
    else:
        form = AvatarFormulario()

    return render(request, "App1/agregarAvatar.html",{"formulario":form})




def inicio(request):
    return render(request, "App1/inicio.html")

def yo(request):
    return render(request, "App1/Acercademi.html")

def Personaje(request):
    return render(request, "App1/personajes.html")



def buscarnickname(request):
    return render(request, "App1/buscarnick.html")

def resultado(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        nicks= personaje.objects.filter(nombre__icontains=nombre)

        return render(request, "App1/resultados.html",{"nicks":nicks, "nombre":nombre})
    else:
        respuesta = "No enviaste datos"


    return HttpResponse(respuesta)

##### Personajes

class ListaPersonaje(LoginRequiredMixin, ListView):
    model = personaje

class DetallePersonaje(LoginRequiredMixin, DetailView):
    model = personaje

class CrearPersonaje(LoginRequiredMixin, CreateView):
    model = personaje
    success_url= "/App1/Personaje/list"
    fields = ["nombre","fuerza","velocidad","resistencia","tipo"]  

class ActualizarPersonaje(LoginRequiredMixin, UpdateView):
    model = personaje
    success_url= "/App1/Personaje/list"
    fields = ["nombre","fuerza","velocidad","resistencia","tipo"]     

class BorrarPersonaje(LoginRequiredMixin, DeleteView):
    model = personaje
    success_url= "/App1/Personaje/list"
    fields = ["nombre","fuerza","velocidad","resistencia","tipo"] 


###### Vestimentas

class ListaVestimenta(LoginRequiredMixin, ListView):
    model = vestimenta

class DetalleVestimenta(LoginRequiredMixin, DetailView):
    model = vestimenta

class CrearVestimenta(LoginRequiredMixin, CreateView):
    model = vestimenta
    success_url= "/App1/Vestimenta/list"
    fields = ["nombre","partesuperior","parteposterior","calzado"]  

class ActualizarVestimenta(LoginRequiredMixin, UpdateView):
    model = vestimenta
    success_url= "/App1/Vestimenta/list"
    fields = ["nombre","partesuperior","parteposterior","calzado"]  
    

class BorrarVestimenta(LoginRequiredMixin, DeleteView):
    model = vestimenta
    success_url= "/App1/Vestimenta/list"
    fields = ["nombre","partesuperior","parteposterior","calzado"]  

##### Armas

class ListaArma(LoginRequiredMixin, ListView):
    model = arma

class DetalleArma(LoginRequiredMixin, DetailView):
    model = arma
class CrearArma(LoginRequiredMixin, CreateView):
    model = arma
    success_url= "/App1/Arma/list"
    fields = ["nombre","tipo","daño","imagen"]  

class ActualizarArma(LoginRequiredMixin, UpdateView):
    model = arma
    success_url= "/App1/Arma/list"
    fields = ["nombre","tipo","daño","imagen"]    
    

class BorrarArma(LoginRequiredMixin, DeleteView):
    model = arma
    success_url= "/App1/Arma/list"
    fields = ["nombre","tipo","daño","imagen"]

#### Escudos

class ListaEscudo(LoginRequiredMixin, ListView):
    model = escudo

class DetalleEscudo(LoginRequiredMixin, DetailView):
    model = escudo 

class CrearEscudo(LoginRequiredMixin, CreateView):
    model = escudo
    success_url= "/App1/Escudo/list"
    fields = ["nombre","durabilidad","imagen"]  

class ActualizarEscudo(LoginRequiredMixin, UpdateView):
    model = escudo
    success_url= "/App1/Escudo/list"
    fields = ["nombre","durabilidad","imagen"]   
    
class BorrarEscudo(LoginRequiredMixin, DeleteView):
    model = escudo
    success_url= "/App1/Escudo/list"
    fields = ["nombre","durabilidad","imagen"]

