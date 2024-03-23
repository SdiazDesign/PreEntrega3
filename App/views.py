from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpRequest
from App.models import *
from App.forms import *
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy, reverse

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request): 

    info = {}
    
    return render(request, "home.html", info)

def aboutme(request): 

    info = {}
    
    return render(request, "aboutme.html", info)

# Partidos
@login_required
def crear_partido(request): 
    
    info = {
        "equipos" : Equipos.objects.all() 
    }

    return render(request, "Partidos/crear_partido.html", info)

@login_required
def grabar_partido(request): 
    
    if request.method == "POST":

        form = PartidosForm(request.POST)
        
        if form.is_valid():
            
            info = form.cleaned_data

            partido = Partidos(
                equipo_local = info["equipo_local"],
                equipo_visitante = info["equipo_visitante"],
                fecha = info["fecha"],
                hora = info["hora"]
            )

            partido.save()

    url_partidos = reverse('partidos')
    
    return redirect(url_partidos)

@login_required
def actualizar_partido(request, pk):
    
    partido = Partidos.objects.get(pk=pk)

    if request.method == "POST":

        form = PartidosForm(request.POST)
        
        if form.is_valid():
            
            info = form.cleaned_data

            partido.equipo_local = info["equipo_local"]
            partido.equipo_visitante = info["equipo_visitante"]
            partido.fecha = info["fecha"]
            partido.hora = info["hora"]
            
            partido.save()

            url_partidos = reverse('partidos')
    
            return redirect(url_partidos)
    else: 
        
        form = PartidosForm(
            initial={
                'equipo_local' : partido.equipo_local,
                'equipo_visitante' : partido.equipo_visitante,
                'fecha' : partido.fecha,
                'hora' : partido.hora
            }
        )

        info = {'form' : form}

        return render(request, "Partidos/actualizar_partido.html", info)

@login_required
def eliminar_partido(request, pk):
    
    if request.method == "POST":
        
        partido = Partidos.objects.get(pk=pk)
        
        partido.delete()

        url_partidos = reverse('partidos')
    
        return redirect(url_partidos)
    
    else: 
       
        partido = Partidos.objects.select_related('equipo_local', 'equipo_visitante').filter(id__iexact=pk)[0]

        info = {
            "pk" : pk,
            "partido" : partido
        }

        return render(request, "Partidos/eliminar_partido.html", info)   

def ver_partido(request, pk):

    # partido = Partidos.objects.select_related('equipo_local', 'equipo_visitante').get(pk=pk)
    partido = Partidos.objects.select_related('equipo_local', 'equipo_visitante').filter(id__iexact=pk)[0]

    info = {
        "partido" : partido
    }

    return render(request, "Partidos/ver_partido.html", info)    


# Resultados
@login_required
def crear_resultado(request): 

    partidos = Partidos.objects.select_related('equipo_local', 'equipo_visitante')

    info = {
        "partidos" : partidos 
    }

    return render(request, "Resultados/crear_resultado.html", info)

@login_required
def grabar_resultado(request): 

    if request.method == "POST":

        form = ResultadosForm(request.POST)
        
        if form.is_valid():
            
            info = form.cleaned_data

            resultado = Resultados(
                partido = info["partido"],
                equipo_local = info["equipo_local"],
                equipo_visitante = info["equipo_visitante"]
            )

            resultado.save()

    url_resultados = reverse('resultados')
    
    return redirect(url_resultados)

@login_required
def actualizar_resultado(request, pk):
    
    resultado = Resultados.objects.get(pk=pk)

    if request.method == "POST":
        
        resultado.equipo_local = request.POST.get("equipo_local")
        resultado.equipo_visitante = request.POST.get("equipo_visitante")
            
        resultado.save()

        url_resultado = reverse('resultados')
    
        return redirect(url_resultado)
    else: 
          
        initial={
            'partido' : resultado.partido,
            'equipo_local' : resultado.equipo_local,
            'equipo_visitante' : resultado.equipo_visitante
        }

        info = {'initial' : initial}

        return render(request, "Resultados/actualizar_resultado.html", info)

@login_required
def eliminar_resultado(request, pk):
    
    if request.method == "POST":
        
        resultado = Resultados.objects.get(pk=pk)
        
        resultado.delete()

        url_resultado = reverse('resultados')
    
        return redirect(url_resultado)
    
    else: 
       
        # resultado = Resultados.objects.select_related('equipo_local', 'equipo_visitante').filter(id__iexact=pk)[0]
        resultado = Resultados.objects.filter(id__iexact=pk)[0]

        info = {
            "pk" : pk,
            "resultado" : resultado
        }

        return render(request, "Resultados/eliminar_resultado.html", info)   

def ver_resultado(request, pk):

    resultado = Resultados.objects.filter(id__iexact=pk)[0]

    info = {
        "resultado" : resultado
    }

    return render(request, "Resultados/ver_resultado.html", info) 


def get_resultado(request):
    id = request.GET.get("partido")

    if id:
        try:

            resultado = Resultados.objects.get(partido=id)
            info = {
                "id" : id,
                "resultado" : resultado,
            }
            return render(request, "Resultados/get_resultado.html", info)
        
        except Resultados.DoesNotExist:
            # El resultado no fue encontrado
            info = {
                "mensaje" : "No se encontró ningún resultado para el partido elegido.",
            }
            return render(request, "home.html", info)
        
    else:
        info = {
            "mensaje" : "No se proporcionó ningún partido.",
        }
        return render(request, "home.html", info)
    
def buscar_resultado(request):

    partidos = Partidos.objects.select_related('equipo_local', 'equipo_visitante')

    info = {
        "partidos" : partidos 
    }

    return render(request, "Resultados/buscar_resultado.html", info)


# Posiciones
@login_required
def crear_posicion(request): 

    info = {
        "equipos" : Equipos.objects.all() 
    }

    return render(request, "Posiciones/crear_posicion.html", info)

@login_required
def grabar_posicion(request): 

    if request.method == "POST":

        form = PosicionesForm(request.POST)
        
        if form.is_valid():
            
            info = form.cleaned_data

            posicion = Posiciones(
                equipo = info["equipo"],
                puntos = info["puntos"]
            )

            posicion.save()

    url_posiciones = reverse('posiciones')
    
    return redirect(url_posiciones)

@login_required
def actualizar_posicion(request, pk):
    
    posicion = Posiciones.objects.get(pk=pk)

    if request.method == "POST":
        
        posicion.puntos = request.POST.get("puntos")
            
        posicion.save()

        url_posiciones = reverse('posiciones')
    
        return redirect(url_posiciones)
    else: 
          
        initial={
            'equipo' : posicion.equipo,
            'puntos' : posicion.puntos
        }

        info = {'initial' : initial}

        return render(request, "Posiciones/actualizar_posicion.html", info)

@login_required
def eliminar_posicion(request, pk):
    
    if request.method == "POST":
        
        posicion = Posiciones.objects.get(pk=pk)
        
        posicion.delete()

        url_posiciones = reverse('posiciones')
    
        return redirect(url_posiciones)
    
    else: 
       
        posicion = Posiciones.objects.filter(id__iexact=pk)[0]

        info = {
            "pk" : pk,
            "posicion" : posicion
        }

        return render(request, "Posiciones/eliminar_posicion.html", info)   

def ver_posicion(request, pk):

    posicion = Posiciones.objects.filter(id__iexact=pk)[0]

    info = {
        "posicion" : posicion
    }

    return render(request, "Posiciones/ver_posicion.html", info) 


###############################################################################
# VBC                                                                         #      
###############################################################################

# Equipo 
class EquipoListView(ListView):
    model = Equipos
    context_object_name = "equipos"
    template_name = "Equipos/lista_de_equipos.html"

class EquipoDetailView(DetailView):
    model = Equipos
    template_name = "Equipos/ver_equipo.html"

class EquipoCreateView(LoginRequiredMixin, CreateView):
    model = Equipos
    template_name = "Equipos/crear_equipo.html"
    # fields = ["nombre", "fechafundacion"]
    form_class = EquiposForm
    success_url = "/App/equipos"
    
class EquipoUpdateView(LoginRequiredMixin, UpdateView):
    model = Equipos
    template_name = "Equipos/editar_equipo.html"
    # fields = ["nombre", "fechafundacion"]
    success_url = "/App/equipos"
    form_class = EquiposForm

class EquipoDeleteView(LoginRequiredMixin, DeleteView):
    model = Equipos
    template_name = "Equipos/borrar_equipo.html"
    success_url = "/App/equipos"

# Partidos 
class PartidoListView(ListView):
    model = Partidos
    context_object_name = "partidos"
    template_name = "Partidos/lista_de_partidos.html"

# Resultados 
class ResultadoListView(ListView):
    model = Resultados
    context_object_name = "resultados"
    template_name = "Resultados/lista_de_resultados.html"

# Posiciones 
class PosicionListView(ListView):
    model = Posiciones
    context_object_name = "posiciones"
    template_name = "Posiciones/lista_de_posicion.html"

class CambiarContra(LoginRequiredMixin, PasswordChangeView):
    template_name = "Registro/cambiar_contra.html"
    success_url = "/App/"


###############################################################################
# Sesiones                                                                    #      
###############################################################################
    
# Iniciar Sesion
def iniciar_sesion(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            info_dic = form.cleaned_data

            usuario = authenticate(
                username=info_dic["username"], 
                password=info_dic["password"]
            )

            if usuario is not None:

                login(request, usuario)

                return render(request, "home.html", {"mensaje":f"Bienvenido {usuario}"})
        
        else:

            return render(request, "home.html", {"mensaje":"Credenciales Incorrectas"})
        
    else:

        form = AuthenticationForm()

        # Agregar clases CSS a los campos del formulario
        for field_name, field in form.fields.items():
            field.widget.attrs['class'] = 'form-control'  # Por ejemplo, asigna la clase 'form-control' a todos los campos

    return render(request, "registro/login.html", {"form":form})

# Registrarse
def registrarse(request):

    if request.method == "POST":

        form = RegistroUsuario(request.POST)

        if form.is_valid():

            form.save() 

            return render(request, "home.html", {"mensaje":"El usuario ha sido creado con éxito."})
    
    else:

        form = RegistroUsuario()

    return render(request, "Registro/registrar.html", {"form":form})

# Agregar Avatar
@login_required
def agregar_avatar(request):

    if request.method == "POST":

        form = AvatarFormulario(request.POST, request.FILES)

        if form.is_valid():

            info = form.cleaned_data

            usuario_actual = User.objects.get(username=request.user)
            nuevo_avatar = Avatar(user=usuario_actual, imagen=info["imagen"])

            nuevo_avatar.save()

            return render(request, "home.html", {"mensaje":"Has creado tu avatar"})
    
    else:

        form = AvatarFormulario()

    return render(request, "registro/nuevo_avatar.html", {"form":form})

# Vista de editar el perfil
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        form = EditarUsuario(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info['email']
            usuario.last_name = info['last_name']
            usuario.first_name = info['first_name']

            usuario.save()

            return render(request, "home.html")

    else:

        form = EditarUsuario(
            initial={
                'username':usuario.username, 
                'first_name':usuario.first_name,
                'last_name':usuario.last_name, 
                'email': usuario.email
            }
        )

    return render(request, "registro/editar_usuario.html", {"form":form})

@login_required
def cerrar_sesion(request):
    
    logout(request)

    return render(request, "home.html", {"mensaje":"Has cerrado sesión con éxito."})