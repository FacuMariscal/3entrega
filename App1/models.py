from django.db import models

class nickname(models.Model):

    nombre = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=20)

class rango(models.Model):
    
    nivel = models.IntegerField()
    liga = models.CharField(max_length=15)
     
class fechadecreacion(models.Model):

    fecha = models.DateField() 
   


