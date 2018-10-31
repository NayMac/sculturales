from django.shortcuts import render

from apps.municipio.forms import MunicipioForm
from apps.municipio.models import Municipio,Estado
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from apps.lugar.forms import LugarForm
from django.http import HttpResponse

# Create your views here.
class Agregar(CreateView):
	model = Municipio
	template_name = 'municipio/municipio_form.html'
	form_class = MunicipioForm
	success_url = reverse_lazy('municipio:listar')


class Editar(UpdateView):
	model = Municipio
	form_class = MunicipioForm
	template_name = 'municipio/municipio_form.html'
	success_url = reverse_lazy('municipio:listar')


class Eliminar(DeleteView):
	model = Municipio
	template_name = 'municipio/municipio_delete.html'
	success_url = reverse_lazy('municipio:listar')


class Listar(ListView):
	model = Municipio
	template_name = 'municipio/municipio_list.html'
