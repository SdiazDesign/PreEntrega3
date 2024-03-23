from django import forms
from App.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class EquiposForm(forms.ModelForm):
    class Meta:
        model = Equipos
        fields = ['nombre', 'fechafundacion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'fechafundacion': forms.DateInput(attrs={'class': 'form-control'}),
        }

class PartidosForm(forms.Form): 
    equipo_local = forms.ModelChoiceField(queryset=Equipos.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    equipo_visitante = forms.ModelChoiceField(queryset=Equipos.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    fecha = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control'}))

class ResultadosForm(forms.Form):
    partido = forms.ModelChoiceField(queryset=Partidos.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    equipo_local = forms.IntegerField(widget=forms.Select(attrs={'class': 'form-control'}))
    equipo_visitante = forms.IntegerField(widget=forms.Select(attrs={'class': 'form-control'}))

class PosicionesForm(forms.Form):
    equipo = forms.ModelChoiceField(queryset=Equipos.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    puntos = forms.IntegerField(widget=forms.Select(attrs={'class': 'form-control'}))

class AvatarFormulario(forms.Form):
    # imagen = forms.ImageField()
    imagen = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

class RegistroUsuario(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",  "email", "password1", "password2"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }    


class EditarUsuario(UserChangeForm):

    password = None

    class Meta:
        model = User
        fields = ["first_name", "last_name",  "email"]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }