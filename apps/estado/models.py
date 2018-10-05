from django.db import models

# Create your models here estado.

from apps.municipio.models import Municipio
class Estado(models.Model):
	name_estado = models.CharField(max_length=50)
	municipio = models.ForeignKey(Municipio, null=True, blank=True, on_delete=models.CASCADE)
