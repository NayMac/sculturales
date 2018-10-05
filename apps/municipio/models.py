from django.db import models

# Create your models here categoria.
from apps.estado.models import Estado

class Municipio(models.Model):
    name_municipio = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, null=True, blank=True, on_delete=models.CASCADE)
