from django.shortcuts import render
from apps.lugar.models import Lugar, Comentario
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from apps.lugar.forms import LugarForm,ComentarioForm
from django.http import HttpResponseRedirect


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


class Comentario(ListView):
    model = Comentario
    template_name = 'lugar/comentario_list.html'

class ComentarioCreate(CreateView):
    model = Comentario
    template_name = 'lugar/comentario_form.html'
    form_class = ComentarioForm
    second_form_class = LugarForm
    success_url = reverse_lazy('lugar:comentar')

def get_context_data(self,**kwargs):
    context = super(ComentarioCreate,self).get_context_data(**kwargs)
    if 'form' not in context:
        context['form'] = self.form_class(self.request.GET)
    if 'form2' not in context:
        context['form2'] = self.second_form_class(self.request.GET)
    return context

def post(self, request, *args,**kwargs):
    self.object = self.get_object
    form = self.form_class(request.POST)
    form2 = self.second_form_class(request.POST)
    if form.is_valid() and form2.is_valid():
        comentario = form.save(commit=False)
        comentario.lugar =form2.save()
        comentario.save()
        return HttpResponseRedirect(self.get_success_url())
    else:
        return self.render_to_response(self.get_context_data(form=form,form2=form2))