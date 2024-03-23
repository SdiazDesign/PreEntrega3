# Generated by Django 5.0.2 on 2024-03-20 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posiciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntos', models.IntegerField()),
                ('equipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.equipos')),
            ],
        ),
    ]
