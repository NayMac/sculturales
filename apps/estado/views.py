from django.shortcuts import render
from django.http import HttpResponse

def index_estado(request):
	return HttpResponse("Segunda pagina de estado")
