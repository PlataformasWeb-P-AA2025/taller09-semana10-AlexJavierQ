# Generated by Django 5.2.4 on 2025-07-28 03:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_campeonato', models.CharField(max_length=100)),
                ('nombre_auspiciante', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('siglas', models.CharField(max_length=10)),
                ('username_twitter', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CampeonatoEquipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año', models.IntegerField(verbose_name='Año del campeonato')),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='los_equipos', to='futbolec.campeonato')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='los_campeonatos', to='futbolec.equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('posicion_campo', models.CharField(max_length=50)),
                ('numero_camiseta', models.IntegerField()),
                ('sueldo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='los_jugadores', to='futbolec.equipo')),
            ],
        ),
    ]
