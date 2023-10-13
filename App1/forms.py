from django import forms


class Formulario1(forms.Form):
     
    nombre= forms.CharField()
    contraseña= forms.CharField()
    nivel= forms.IntegerField()
    liga= forms.CharField()
    fecha= forms.DateField()
    email= forms.EmailField()

class Formulario2(forms.Form):
    name= forms.CharField()
    fuerza= forms.IntegerField()
    velocidad= forms.IntegerField()
    resistencia= forms.IntegerField()
    tipo= forms.CharField()    
