from django.contrib import admin
from apps.lugar.models import Categoria,Estado,Municipio,Lugar

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Estado)
admin.site.register(Municipio)
admin.site.register(Lugar)