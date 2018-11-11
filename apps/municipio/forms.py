from django import forms
from apps.municipio.models import Municipio,Estado

class MunicipioForm(forms.ModelForm):
    class Meta:
        model = Municipio
        fields = [
            'name_municipio',
            'estado',
        ]
        labels = {
            'name_municipio': 'Municipio',
            'estado':'Estado',
        }
        widgets = {
            'name_municipio': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }