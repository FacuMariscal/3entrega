from django.contrib import admin
from django.urls import path
from App1.views import *

urlpatterns = [
    path("",inicio, name="Inicio"),
    path("Usuarios", Usuario, name="Usuarios"),
    path("Formulario/", formulario, name="Formulario"),
    path("Buscarnick", buscarnickname, name="buscarnick"),
    path("resultados/", resultado, name="Resultadonick"),

    #CRUD de personajes

    path("Personaje/list/", ListaPersonaje.as_view(), name="PersonajeLista"),
    path("Personaje/<int:pk>", DetallePersonaje.as_view(), name="PersonajeDetalle"),
    path("Personaje/crear/", CrearPersonaje.as_view(), name="PersonajeCrear"),
    path("Personaje/editar/<int:pk>", ActualizarPersonaje.as_view(), name="PersonajeEditar"),
    path("Personaje/eliminar/<int:pk>", BorrarPersonaje.as_view(), name="PersonajeEliminar"),




]   