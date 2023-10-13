from django.db import models

class usuario(models.Model):

    def __str__(self):
        return f"{self.nombre}"

    nombre = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=20)
    nivel = models.IntegerField()
    liga = models.CharField(max_length=15)
    fecha = models.DateField() 
    email = models.EmailField()
    
class personaje(models.Model):

    def __str__(self):
        return f"{self.name}"

    name = models.CharField(max_length=20)
    fuerza = models.IntegerField()
    velocidad = models.IntegerField()
    resistencia = models.IntegerField()
    tipo = models.CharField(max_length=20)

class vestimenta(models.Model):
    def __str__(self):
        return f"{self.nombre}"
    
    nombre = models.CharField(max_length=20)
    partesuperior = models.ImageField()
    parteposterior = models.ImageField()
    calzado = models.ImageField()
    

   


