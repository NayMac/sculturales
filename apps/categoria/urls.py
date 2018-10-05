from django.urls import include, path
from apps.categoria.views import *
# categoria <int:id_categoria>

app_name = 'categoria'

urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', CatAgregar.as_view(), name='categoria_crear'),
    path('listar/', CatList.as_view(), name='categoria_listar'),
    path('editar/<pk>/', CatEdit.as_view(), name='categoria_editar'),
    path('eliminar/<pk>/', CatEdit.as_view(), name='categoria_delete'),
]