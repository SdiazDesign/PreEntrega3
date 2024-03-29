# Generated by Django 5.0.2 on 2024-03-04 12:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_partidos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipo_local', models.IntegerField()),
                ('equipo_visitante', models.IntegerField()),
                ('partido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.partidos')),
            ],
        ),
    ]
