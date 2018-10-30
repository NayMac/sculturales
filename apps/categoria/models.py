from django.db import models

# Create your models here categoria.
class Categoria(models.Model):
	name_categoria = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.name_categoria)