from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Pupuseria juan Perez')

def home(requets):
    return render(requets,'inicio.html')