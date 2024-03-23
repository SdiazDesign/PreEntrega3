from django.urls import path
from App.views import *

urlpatterns = [
    
    # VBC              
    path('equipos/', EquipoListView.as_view(), name="equipos"),
    path('nuevo_equipo/', EquipoCreateView.as_view(), name="nuevo_equipo"),
    path('editar_equipo/<int:pk>', EquipoUpdateView.as_view(), name="editar_equipo"),
    path('eliminar_equipo/<int:pk>', EquipoDeleteView.as_view(), name="eliminar_equipo"),
    path('ver_equipo/<int:pk>', EquipoDetailView.as_view(), name="ver_equipo"),

    # Se reemplazan por las anteriores 
    # path('crear_equipo/', crear_equipo, name="crear_equipo"),
    # path('grabar_equipo/', grabar_equipo, name="grabar_equipo"),
    # path('actualizar_equipo/<id_equipo>', actualizar_equipo, name="actualizar_equipo"),

    path('partidos/', PartidoListView.as_view(), name="partidos"),
    path('crear_partido/', crear_partido, name="crear_partido"),
    path('grabar_partido/', grabar_partido, name="grabar_partido"),
    path('actualizar_partido/<int:pk>', actualizar_partido, name="actualizar_partido"),
    path('eliminar_partido/<int:pk>', eliminar_partido, name="eliminar_partido"),
    path('ver_partido/<int:pk>', ver_partido, name="ver_partido"),
    
    path('resultados/', ResultadoListView.as_view(), name="resultados"),
    path('crear_resultado/', crear_resultado, name="crear_resultado"),
    path('grabar_resultado/', grabar_resultado, name="grabar_resultado"),
    path('actualizar_resultado/<int:pk>', actualizar_resultado, name="actualizar_resultado"),
    path('eliminar_resultado/<int:pk>', eliminar_resultado, name="eliminar_resultado"),
    path('ver_resultado/<int:pk>', ver_resultado, name="ver_resultado"),

    path('get_resultado/', get_resultado, name="get_resultado"),
    path('buscar_resultado/', buscar_resultado, name="buscar_resultado"),

    path('posiciones/', PosicionListView.as_view(), name="posiciones"),
    path('crear_posicion/', crear_posicion, name="crear_posicion"),
    path('grabar_posicion/', grabar_posicion, name="grabar_posicion"),
    path('actualizar_posicion/<int:pk>', actualizar_posicion, name="actualizar_posicion"),
    path('eliminar_posicion/<int:pk>', eliminar_posicion, name="eliminar_posicion"),
    path('ver_posicion/<int:pk>', ver_posicion, name="ver_posicion"),
    

    path("login/",iniciar_sesion, name="login"),
    path("registrarse/",registrarse, name="registrarse"),
    path("cerrar_sesion/",cerrar_sesion, name="cerrar_sesion"),
    path("edit/", editarPerfil, name="Editar Usuario"),
    path("contra/", CambiarContra.as_view(), name="Cambiar Contraseña"),
    path("avatar/", agregar_avatar, name="Agregar Avatar"),

    path("aboutme/",aboutme, name="aboutme"),
    
    path('', home, name="home"),
]