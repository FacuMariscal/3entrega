from django.contrib import admin
from django.urls import path
from App1.views import *

urlpatterns = [
    path("",inicio, name="Inicio"),
    path("Usuarios", Usuario, name="Usuarios"),
    path("Formulario/", formulario, name="Formulario"),
    path("Buscarnick", buscarnickname, name="buscarnick"),
    path("resultados/", resultado, name="Resultadonick"),
    path("Formulario2/", formulario2, name="Formulario2"),
    path("Personajes/", Personaje, name= "Personaje"),
]