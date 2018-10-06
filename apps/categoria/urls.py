from django.urls import path
from apps.categoria.views import *

app_name = 'categoria'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('nuevo/', Agregar.as_view(), name='crear'),
    path('editar/<pk>/', Editar.as_view(), name='editar'),
    path('eliminar/<pk>/', Eliminar.as_view(), name='eliminar'),
    path('listar/', Listar.as_view(), name='listar'),
]
