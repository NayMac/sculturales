from django import forms
from apps.categoria.models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
            'name_categoria',
        ]
        labels = {
            'name_categoria':'Nombre Categoria'
        }
        widgets = {
            'name_categoria': forms.TextInput(attrs={'class':'form-control'}),
        }