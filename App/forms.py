from django import forms
from App.models import *

class EquiposForm(forms.Form): 
    nombre = forms.CharField(max_length=30)
    fechafundacion = forms.DateField()

class PartidosForm(forms.Form): 
    equipo_local = forms.ModelChoiceField(queryset=Equipos.objects.all())
    equipo_visitante = forms.ModelChoiceField(queryset=Equipos.objects.all())
    fecha = forms.DateField()
    hora = forms.TimeField()

class ResultadosForm(forms.Form):
    partido = forms.ModelChoiceField(queryset=Partidos.objects.all())
    equipo_local = forms.IntegerField()
    equipo_visitante = forms.IntegerField()