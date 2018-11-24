from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import reverse_lazy, LoginView, LogoutView
from django.urls import reverse_lazy
from django.conf import settings
from apps.usuario.forms import RegistroForm, LoginForm
from apps.usuario.serializers import UserSerializer
from django.http import HttpResponse, HttpResponseRedirect
import json
from rest_framework.views import APIView


class RegistroUsuario(CreateView):
    model = User
    template_name = 'usuario/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('lugar:listar')

class Login(LoginView):
    form_class = LoginForm
    template_name = 'usuario/login.html'
    success_url = reverse_lazy('lugar:listar')

    def form_valid(self, form):
        login(self.request,form.get_user())
        return HttpResponseRedirect(self.success_url)

class Logout(LogoutView):
    success_url =reverse_lazy('lugar:listar')
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        success_url = self.success_url
        if success_url:
            return HttpResponseRedirect(success_url)
        return super().dispatch(request,*args,**kwargs)
