from django.db import models

# Create your models here categoria.
from apps.categoria.models import Categoria
from apps.estado.models import Estado
from apps.municipio.models import Municipio

class Lugar(models.Model):
    name_lugar = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()
    categoria = models.ForeignKey(Categoria,null=True,blank=True,on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado,null=True,blank=True,on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio,null=True,blank=True,on_delete=models.CASCADE)

