from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from decimal import Decimal
from .models import pagoPupas

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

def pagos(request): 
    if request.method == 'POST': 
        cantidadPupusas = int(request.POST['cantidadPupusas'])
        tipoDePupusa = request.POST['tipoDePupusa']
        cantidadBebida = int(request.POST['cantidadBebida'])
        tipoDeBebida = request.POST['tipoDeBebida']
        correoCliente = request.POST['correoCliente']
        pagaCon = Decimal(request.POST['pagaCon'])

        # Calcular el precio de las pupusas y bebidas
        precio_pupusa = {'Frijol': 0.35, 'Queso': 0.50, 'Revuelta': 0.75}.get(tipoDePupusa, 0)
        precio_bebida = {'Sin bebida': 0, 'Bolsa con agua': 0.25, 'Refresco': 0.50, 'Jugo Natural': 1.00}.get(tipoDeBebida, 0)

        # Calcular el total
        total_pupusas = precio_pupusa * cantidadPupusas
        total_bebidas = precio_bebida * cantidadBebida
        total = total_pupusas + total_bebidas

        # Guardar los datos en la base de datos
        # Guardar los datos en la base de datos
        pedido = pagoPupas(
            cantidadPupusas=cantidadPupusas,
            tipoDePupusa=tipoDePupusa,
            cantidadBebida=cantidadBebida,
            tipoDeBebida=tipoDeBebida,
            correoCliente=correoCliente,
            pagaCon=pagaCon,
            total=total  # Asegúrate de que este campo esté definido en tu modelo
        )
        pedido.save()

        # Renderizar una respuesta o redireccionar a una página de confirmación
        return render(request, 'confirmacion.html', {'pedido': pedido})
    
    return render(request, 'formulario_pagos.html')

def home(request):
    return render(request,'inicio.html')

def pagos(request):
    return render(request, 'pagos.html')

def reportes(request):
    return render(request,'reportes.html' )

def inven(request):
    return render(request, 'inventario.html')