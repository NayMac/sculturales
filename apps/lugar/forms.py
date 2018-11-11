from django import forms
from apps.lugar.models import Lugar,Comentario

class LugarForm (forms.ModelForm):
    class Meta:
        model = Lugar
        fields = [
            'name_lugar',
            'direccion',
            'telefono',
            'categoria',
            'municipio',
        ]
        labels = {
            'name_lugar': 'Nombre del Lugar',
            'direccion': 'Dirección',
            'telefono':'Telefono',
            'categoria':'Categoria',
            'municipio':'Municipio'

        }
        widgets = {
            'name_lugar': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'municipio': forms.Select(attrs={'class': 'form-control'}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = [
            'name_persona',
            'comentario',
            'email',
        ]
        labels = {
            'name_persona':'Nombre(s),Apellido(s)',
            'comentario':'Comentario',
            'email':'Correo electronico',
        }
        widgets = {
            'name_persona': forms.TextInput(attrs={'class':'form-control'}),
            'comentario': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
        }