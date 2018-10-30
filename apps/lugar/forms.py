from django import forms
from apps.lugar.models import Lugar

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
            'name_lugar': 'Nombre Estado',
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