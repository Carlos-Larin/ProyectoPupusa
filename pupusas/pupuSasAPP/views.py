from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.

#def index(request):
    #return HttpResponse('Pupuseria juan Perez')

def sesion(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirigir a la vista deseada después del inicio de sesión
            else:
            # Manejo de error: credenciales incorrectas
                error_message = "Usuario o contraseña incorrectos."
                return render(request, 'registration/login.html', {'error_message': error_message})

    return render(request, 'registration/login.html') 



def home(request):
    return render(request,'inicio.html')

def pagos(request):
    return render(request, 'pagos.html')

def reportes(request):
    return render(request,'reportes.html' )

def inven(request):
    return render(request, 'inventario.html')