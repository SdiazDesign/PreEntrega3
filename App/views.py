from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from App.models import *
from App.forms import *

def home(request): 

    info = {}
    
    return render(request, "home.html", info)

def crear_partido(request): 
    
    info = {
        "equipos" : Equipos.objects.all() 
    }

    return render(request, "crear_partido.html", info)

def crear_equipo(request): 
    
    info = {}

    return render(request, "crear_equipo.html", info)

def crear_resultado(request): 

    partidos = Partidos.objects.select_related('equipo_local', 'equipo_visitante')

    info = {
        "partidos" : partidos 
    }

    return render(request, "crear_resultado.html", info)

def grabar_equipo(request): 
    
    if request.method == "POST":

        form = EquiposForm(request.POST)

        if form.is_valid():

            info = form.cleaned_data
            
            equipo = Equipos(
                nombre = info["nombre"],
                fechafundacion = info["fechafundacion"]
            )

            equipo.save()

    return render(request, "home.html")

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

    return render(request, "home.html")

def grabar_resultado(request): 
    if request.method == "POST":

        form = ResultadosForm(request.POST)
        
        if form.is_valid():
            
            info = form.cleaned_data

            partido = Resultados(
                partido = info["partido"],
                equipo_local = info["equipo_local"],
                equipo_visitante = info["equipo_visitante"]
            )

            partido.save()

    return render(request, "home.html")





def buscar_equipo(request):

    id = request.GET["id"]

    if id:
        equipos = Equipos.objects.filter(id__iexact=id)

        #return HttpResponse(cursos)

        info = {
            "id" : id,
            "equipos" : equipos,
        }

        return render(request, "resultados_busqueda_equipo.html", info)
    
    else : 

        response = "No enviaste datos"

        return HttpResponse(response)
