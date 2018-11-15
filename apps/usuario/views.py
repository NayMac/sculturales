from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import reverse_lazy
from django.urls import reverse_lazy

from django.conf import settings



from apps.usuario.forms import RegistroForm
from apps.usuario.serializers import UserSerializer
from django.http import HttpResponse
import json
from rest_framework.views import APIView

class RegistroUsuario(CreateView):
    model = User
    template_name = "usuario/registrar.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('lugar:lugar_listar')

class UserAPI(APIView):
    serializer = UserSerializer
    def get(self, request, format=None):
        lista = User.objects.all()
        response = self.serializer(lista, many=True)
        return HttpResponse(json.dumps(response.data), content_type='application/json')