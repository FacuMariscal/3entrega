from django.contrib import admin
from django.urls import path
from App1.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("login", iniciosesion, name="login"),
    path("registro", registro, name="Registro"),
    path("",inicio, name="Inicio"),
    path("Buscarnick", buscarnickname, name="buscarnick"),
    path("resultados/", resultado, name="Resultadonick"),
    path("logout", LogoutView.as_view(template_name="App1/logout.html"), name="Logout"),

    #CRUD de personajes

    path("Personaje/list/", ListaPersonaje.as_view(), name="PersonajeLista"),
    path("Personaje/<int:pk>", DetallePersonaje.as_view(), name="PersonajeDetalle"),
    path("Personaje/crear/", CrearPersonaje.as_view(), name="PersonajeCrear"),
    path("Personaje/editar/<int:pk>", ActualizarPersonaje.as_view(), name="PersonajeEditar"),
    path("Personaje/eliminar/<int:pk>", BorrarPersonaje.as_view(), name="PersonajeEliminar"),

    #CRUD de usuarios

    path("Usuario/list/", ListaUsuario.as_view(), name= "UsuarioLista"),
    path("Usuario/<int:pk>", DetalleUsuario.as_view(), name= "UsuarioDetalle"),
    path("Usuario/crear/", CrearUsuario.as_view(), name= "UsuarioCrear"),
    path("Usuario/editar/<int:pk>", ActualizarUsuario.as_view(), name= "UsuarioEditar"),
    path("Usuario/eliminar/<int:pk>", BorrarUsuario.as_view(), name= "UsuarioEliminar"),




]


