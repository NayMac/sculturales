from django.shortcuts import render
from django.http import HttpResponse
from apps.estado.forms import EstadoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from apps.estado.models import Estado

def index_estado(request):
	return HttpResponse("Segunda pagina de estado")

class Agregar(CreateView):
	model = Estado
	template_name = 'estado/estado_form.html'
	form_class = EstadoForm
	success_url = reverse_lazy('estado:listar')


class Editar(UpdateView):
	model = Estado
	form_class = EstadoForm
	template_name = 'estado/estado_form.html'
	success_url = reverse_lazy('estado:listar')


class Eliminar(DeleteView):
	model = Estado
	template_name = 'estado/estado_delete.html'
	success_url = reverse_lazy('estado:listar')


class Listar(ListView):
	model = Estado
	template_name = 'estado/estado_list.html'
