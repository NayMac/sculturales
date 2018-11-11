from django.db import models

# Create your models here estado.
class Estado(models.Model):
    name_estado = models.CharField(max_length=50)
    def __str__(self):
        return '{}'.format(self.name_estado)