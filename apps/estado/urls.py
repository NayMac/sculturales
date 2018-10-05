from django.conf.urls import url, include
from apps.estado.views import index_estado

urlpatterns = [
    url(r'^$', index_estado),
]