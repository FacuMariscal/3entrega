from django.db import models
from django.contrib.auth.models import User
  
class personaje(models.Model):

    def __str__(self):
        return f"{self.nombre}"

    nombre = models.CharField(max_length=20)
    fuerza = models.IntegerField()
    velocidad = models.IntegerField()
    resistencia = models.IntegerField()
    tipo = models.CharField(max_length=20)

class vestimenta(models.Model):
    def __str__(self):
        return f"{self.nombre}"
    
    nombre = models.CharField(max_length=20)
    partesuperior = models.ImageField(upload_to="ropa", null=True,blank=True)
    parteposterior = models.ImageField(upload_to="ropa", null=True,blank=True)
    calzado = models.ImageField(upload_to="ropa", null=True,blank=True)

class arma(models.Model):
    def __str__(self):
        return f"{self.nombre}"
    
    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    daño = models.IntegerField()
    imagen = models.ImageField(upload_to="armas", null=True,blank=True)

class escudo(models.Model):
    def __str__(self):
        return f"{self.nombre}"
    
    nombre = models.CharField(max_length=20)
    durabilidad = models.IntegerField()
    imagen = models.ImageField(upload_to="escudos", null=True,blank=True)
    
class avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)


   


