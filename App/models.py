from django.db import models

class Equipos(models.Model):
    nombre = models.CharField(max_length=30)
    fechafundacion = models.DateField()

class Partidos(models.Model):
    equipo_local = models.ForeignKey(Equipos, name="equipo_local", on_delete=models.SET_NULL, null=True, related_name='equipo_local')
    equipo_visitante = models.ForeignKey(Equipos, name="equipo_visitante", on_delete=models.SET_NULL, null=True, related_name='equipo_visitante')
    fecha = models.DateField()
    hora = models.TimeField()

class Resultados(models.Model):
    partido = models.ForeignKey(Partidos, on_delete=models.SET_NULL, null=True)
    equipo_local = models.IntegerField()
    equipo_visitante = models.IntegerField()
    
"""      
class Posiciones(models.Model):
    equipo = models.ForeignKey('Equipos', on_delete=models.SET_NULL, null=True)
    puntos = models.IntegerField()
"""