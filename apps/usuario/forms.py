from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from numpy.core.defchararray import strip

class RegistroForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
			]
		labels = {
				'username': 'Nombre de usuario',
				'first_name': 'Nombre',
				'last_name': 'Apellidos',
				'email': 'Correo',
            }
widgets = {
                'username': forms.TextInput(attrs={'class': 'form-control'}),
                'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                'email': forms.TextInput(attrs={'class': 'form-control'}),

            }

class LoginForm(AuthenticationForm):
	username = UsernameField(widget=forms.TextInput( attrs={
		'autofocus':True,
		'class':'for-control',
		'placeholder':'Codigo'

	}))
	password = forms.CharField(
		strip=False,
		widget=forms.PasswordInput(attrs={
		'class':'form-control',
		'placeholder':'Contraseña'
	}))