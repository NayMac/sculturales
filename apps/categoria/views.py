# from django.shortcuts import render, redirect
from apps.categoria.forms import CategoriaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from apps.categoria.models import Categoria
from django.urls import reverse_lazy


class Index(TemplateView):
    template_name = 'categoria/index.html'

class Agregar(CreateView):
    model = Categoria
    template_name = "categoria/categoria_form.html"
    form_class = CategoriaForm
    success_url = reverse_lazy('categoria:listar')


class Editar(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/categoria_form.html'
    success_url = reverse_lazy('categoria:listar')


class Eliminar(DeleteView):
    model = Categoria
    template_name = "categoria/categoria_delete.html"
    success_url = reverse_lazy('categoria:listar')


class Listar(ListView):
    model = Categoria
    template_name = "categoria/categoria_list.html"
