from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#def index(request):
    #return HttpResponse('Pupuseria juan Perez')

def home(requets):
    return render(requets,'inicio.html')

def pagos(request):
    return render(request, 'pagos.html')

def reportes(request):
    return render(request,'reportes.html' )

def inven(request):
    return render(request, 'inventario.html')