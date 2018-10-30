from django.shortcuts import render
from apps.lugar.models import Lugar
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from apps.lugar.forms import LugarForm
from django.http import HttpResponse

# Create your views here.
class Agregar(CreateView):
	model = Lugar
	template_name = 'lugar/lugar_form.html'
	form_class = LugarForm
	success_url = reverse_lazy('lugar:listar')


class Editar(UpdateView):
	model = Lugar
	form_class = LugarForm
	template_name = 'lugar/lugar_form.html'
	success_url = reverse_lazy('lugar:listar')


class Eliminar(DeleteView):
	model = Lugar
	template_name = 'lugar/lugar_delete.html'
	success_url = reverse_lazy('lugar:listar')


class Listar(ListView):
	model = Lugar
	template_name = 'lugar/lugar_list.html'
