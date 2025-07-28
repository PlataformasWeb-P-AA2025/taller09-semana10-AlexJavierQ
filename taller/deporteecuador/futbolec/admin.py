# futbolec/admin.py

from django.contrib import admin
from .models import Equipo, Jugador, Campeonato, CampeonatoEquipos

# Registrar los modelos para que aparezcan en el admin
admin.site.register(Equipo)
admin.site.register(Jugador)
admin.site.register(Campeonato)
admin.site.register(CampeonatoEquipos)