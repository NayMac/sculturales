from django.db import models

# Create your models here categoria.
class Municipio(models.Model):
    name_municipio = models.CharField(max_length=50)

