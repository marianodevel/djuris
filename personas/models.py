from django.db import models

# from djuris_legal.causas.models import Causa


class Persona(models.Model):
    apellido = models.CharField(max_length=25)
    nombre = models.CharField(max_length=50)
    dni = models.IntegerField()
    direccion = models.CharField(max_length=50)


class Cliente(Persona):
    pass


class Contraparte(Persona):
    pass


class Tercero(Persona):
    pass
