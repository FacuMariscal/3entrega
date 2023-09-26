from django.contrib import admin
from django.urls import path
from App1.views import *

urlpatterns = [
    path("",inicio, name="Inicio"),
    path("Usuarios", Usuario, name="Usuarios"),
    path("Rangos", Rango, name="Rangos"),
    path("Fechadecreacion", FechaDeCreacion, name="Fechasdecreacion"),
    path("Formulario/", formulario, name="Formulario"),
    path("Buscarnick", buscarnickname, name="buscarnick"),
    path("resultados/", resultado, name="Resultadonick"),
]