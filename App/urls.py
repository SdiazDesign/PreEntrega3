from django.urls import path
from App.views import *

urlpatterns = [
    path('crear_equipo/', crear_equipo, name="crear_equipo"),
    path('grabar_equipo/', grabar_equipo, name="grabar_equipo"),
    path('crear_partido/', crear_partido, name="crear_partido"),
    path('grabar_partido/', grabar_partido, name="grabar_partido"),
    path('crear_resultado/', crear_resultado, name="crear_resultado"),
    path('grabar_resultado/', grabar_resultado, name="grabar_resultado"),
    # path('get_resultado/', get_resultado, name="get_resultado"),
    # path('buscar_resultado/', buscar_resultado, name="resultado_buscar_resultado"),
    path('', home, name="home"),
]