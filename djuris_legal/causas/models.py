from django.db import models
from django.utils.translation import gettext_lazy as _


class Objeto(models.TextChoices):
    ALIMENTOS = "AL", _("Alimentos")
    CUIDADO = "CP", _("Cuidado Personal")
    DIVORCIO = "DV", _("Divorcio Vincular")
    SUCESION = "Su", _("Sucesion")


class Fuero(models.TextChoices):
    FAMILIA = "Fam", _("Familia")
    CIVIL = "Civ", _("Civil")
    PENAL = "Pen", _("Penal")


class Movimiento(models.Model):
    class TipoMovimiento(models.TextChoices):
        INICIO = _("inicio")
        TRAMITE = _("mero tramite")
        RECURSO = _("recurso")

    fecha = models.DateField()
    tipo = models.CharField(choices=TipoMovimiento.choices, default=None)
    causa = models.ForeignKey("causas", on_delete=models.CASCADE, blank=False)


class Causa(models.Model):
    caratula = models.CharField(max_length=100)
    expediente = models.IntegerField()
    año = models.IntegerField()
    actora = models.CharField(max_length=50)
    demandada = models.CharField(max_length=50)
    fuero = models.CharField(choices=Fuero.choices, default=None)
    objeto = models.CharField(choices=Objeto.choices, default=None)

    def __str__(self):
        return str(self.caratula)
