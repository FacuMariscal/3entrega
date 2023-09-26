from django import forms


class Formulario1(forms.Form):
     
    nombre= forms.CharField()
    contraseña= forms.CharField()
    nivel= forms.IntegerField()
    liga= forms.CharField()
    fecha= forms.DateField()
