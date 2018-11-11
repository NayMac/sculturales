from django.db import models

# Create your models here categoria.
from apps.categoria.models import Categoria
from apps.municipio.models import Municipio


class Lugar(models.Model):
    name_lugar = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, null=True, blank=True, on_delete=models.CASCADE)


class Comentario(models.Model):
    name_persona = models.CharField(max_length=100)
    comentario = models.CharField(max_length=250)
    email = models.CharField(max_length=50)
