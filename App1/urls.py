from django.contrib import admin
from django.urls import path
from App1.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from App1.forms import *


urlpatterns = [
    path("login/", iniciosesion, name="login"),
    path("registro/", registro, name="Registro"),
    path("agregar/", agregarAvatar, name="Avatarimagen"),
    path("",inicio, name="Inicio"),
    path("Acercademi",yo, name="Acercademi"),
    path("Buscarnick", buscarnickname, name="buscarnick"),
    path("resultados/", resultado, name="Resultadonick"),
    path("logout", LogoutView.as_view(template_name="App1/logout.html"), name="Logout"),
    path("editar/",editarUsuario, name = "EditarUsuario"),

    #CRUD de personajes

    path("Personaje/list/", ListaPersonaje.as_view(), name="PersonajeLista"),
    path("Personaje/<int:pk>", DetallePersonaje.as_view(), name="PersonajeDetalle"),
    path("Personaje/crear/", CrearPersonaje.as_view(), name="PersonajeCrear"),
    path("Personaje/editar/<int:pk>", ActualizarPersonaje.as_view(), name="PersonajeEditar"),
    path("Personaje/eliminar/<int:pk>", BorrarPersonaje.as_view(), name="PersonajeEliminar"),

    #CRUD de vestimenta

    path("Vestimenta/list/", ListaVestimenta.as_view(), name= "VestimentaLista"),
    path("Vestimenta/<int:pk>", DetalleVestimenta.as_view(), name = "VestimentaDetalle"),
    path("Vestimenta/crear/", CrearVestimenta.as_view(), name = "VestimentaCrear"),
    path("Vestimenta/editar/<int:pk>", ActualizarVestimenta.as_view(), name = "VestimentaEditar"),
    path("Vestimenta/eliminar/<int:pk>", BorrarVestimenta.as_view(), name= "VestimentaEliminar"),
    
    #CRUD de arma

    path("Arma/list", ListaArma.as_view(), name= "ArmaLista"),
    path("Arma/<int:pk>", DetalleArma.as_view(), name = "ArmaDetalle"),
    path("Arma/crear/", CrearArma.as_view(), name = "ArmaCrear"),
    path("Arma/editar/<int:pk>", ActualizarArma.as_view(), name = "ArmaEditar"),
    path("Arma/eliminar/<int:pk>", BorrarArma.as_view(), name= "ArmaEliminar"),

    #CRUD de escudo
    
    path("Escudo/list", ListaEscudo.as_view(), name= "EscudoLista"),
    path("Escudo/<int:pk>", DetalleEscudo.as_view(), name = "EscudoDetalle"),
    path("Escudo/crear/", CrearEscudo.as_view(), name = "EscudoCrear"),
    path("Escudo/editar/<int:pk>", ActualizarEscudo.as_view(), name = "EscudoEditar"),
    path("Escudo/eliminar/<int:pk>", BorrarEscudo.as_view(), name= "EscudoEliminar"),

]


