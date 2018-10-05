from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.categoria.forms import CategoriaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.categoria.models import Categoria
from django.urls import reverse_lazy


class CatList(ListView):
    model = Categoria
    template_name = "categoria/categoria_list.html"


class CatAgregar(CreateView):
    model = Categoria
    template_name = "categoria/categoria_form.html"
    form_class = CategoriaForm
    success_url = reverse_lazy('categoria:categoria_listar')


class CatEdit(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "categoria/categoria_form.html"

    def post(self, request, *args, **kwargs):
        reverse_lazy('categoria:categoria_listar')


class CatEliminar(DeleteView):
    model = Categoria
    template_name = "categoria/categoria_delete.html"
    success_url = "listar"


def index(request):
    return render(request, 'categoria/index.html')


def categoria_view(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria:index')
    else:
        form = CategoriaForm()
    return render(request, 'categoria/categoria_form.html', {'form': form})


def categoria_list(request):
    categoria = Categoria.objects.all()
    contexto = {'categorias': categoria}
    return render(request, 'categoria/categoria_list.html', contexto)


def categoria_edit(request, id_categoria):
    categoria = Categoria.objects.get(id=id_categoria)
    if request.method == 'GET':
        form = CategoriaForm(instance=categoria)
    else:
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('categoria/categoria_list.html'))
    return render(request, 'categoria/categoria_form.html', {'form': form})
