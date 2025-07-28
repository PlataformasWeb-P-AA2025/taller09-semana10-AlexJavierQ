# futbolec/models.py

from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    siglas = models.CharField(max_length=10)
    username_twitter = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.siglas}) - @{self.username_twitter}"

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion_campo = models.CharField(max_length=50)
    numero_camiseta = models.IntegerField()
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE,
                               related_name='los_jugadores')

    def __str__(self):
        return (f"{self.nombre} - {self.posicion_campo} ({self.numero_camiseta}) "
                f"- Equipo: {self.equipo.nombre}")

class Campeonato(models.Model):
    nombre_campeonato = models.CharField(max_length=100)
    nombre_auspiciante = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre_campeonato} (Auspiciante: {self.nombre_auspiciante})"

class CampeonatoEquipos(models.Model):
    año = models.IntegerField("Año del campeonato")
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE,
                               related_name='los_campeonatos')
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE,
                                   related_name='los_equipos')

    def __str__(self):
        return f"Año: {self.año} - {self.equipo.nombre} ({self.campeonato.nombre_campeonato})"