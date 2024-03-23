from django.db import models
from django.contrib.auth.models import User 

class Equipos(models.Model):
    nombre = models.CharField(max_length=30)
    fechafundacion = models.DateField()

    def __str__(self):
        return f"{self.nombre}"

class Partidos(models.Model):
    equipo_local = models.ForeignKey(Equipos, name="equipo_local", on_delete=models.SET_NULL, null=True, related_name='equipo_local')
    equipo_visitante = models.ForeignKey(Equipos, name="equipo_visitante", on_delete=models.SET_NULL, null=True, related_name='equipo_visitante')
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.equipo_local} VS {self.equipo_visitante}"

class Resultados(models.Model):
    partido = models.ForeignKey(Partidos, on_delete=models.SET_NULL, null=True)
    equipo_local = models.IntegerField()
    equipo_visitante = models.IntegerField()

    def __str__(self):
        return f"{self.equipo_local} - {self.equipo_visitante} "

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    
class Posiciones(models.Model):
    equipo = models.ForeignKey('Equipos', on_delete=models.SET_NULL, null=True)
    puntos = models.IntegerField()
    def __str__(self):
        return f"{self.equipo} - {self.puntos}"