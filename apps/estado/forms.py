from django import forms
from apps.estado.models import Estado

class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = [
            'name_estado',
        ]
        labels = {
            'name_estado': 'Nombre Estado'
        }
        widgets = {
            'name_estado': forms.TextInput(attrs={'class': 'form-control'}),
        }