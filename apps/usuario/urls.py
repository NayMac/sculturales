from django.contrib import admin
from django.urls import path
from apps.usuario.views import RegistroUsuario,Logout,Login
app_name = 'usuario'
urlpatterns = [
    path('registrar', RegistroUsuario.as_view(), name="registrar"),
    path('login', Login.as_view(), name="login"),

]