from django.urls import path
from apps.estado.views import *
app_name = 'estado'

urlpatterns = [
   # url(r'^$', index_estado),
    path('nuevo/', Agregar.as_view(), name='crear'),
    path('editar/<pk>/', Editar.as_view(), name='editar'),
    path('eliminar/<pk>/', Eliminar.as_view(), name='eliminar'),
    path('listar/', Listar.as_view(), name='listar'),
]