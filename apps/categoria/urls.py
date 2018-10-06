from django.urls import include, path
from apps.categoria.views import *
# categoria <int:id_categoria>

app_name = 'categoria'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('nuevo/', Agregar.as_view(), name='crear'),
    path('editar/<pk>/', Editar.as_view(), name='editar'),
    path('eliminar/<pk>/', Eliminar.as_view(), name='eliminar'),
    path('listar/', Listar.as_view(), name='listar'),
]