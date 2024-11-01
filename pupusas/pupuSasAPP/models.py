from django.db import models

# Create your models here.
class pagoPupas(models.Model):
    cantidadPupusas= models.IntegerField()
    tipoDePupusa = models.CharField(max_length=50)
    cantidadBebida= models.IntegerField()
    tipoDeBebida = models.CharField(max_length=50)
    correoCliente= models.EmailField(max_length=200)
    pagaCon = models.DecimalField(max_digits=10, decimal_places=4)

def __str__(self):
        return f"Pedido de {self.cantidadPupusas} pupusas y {self.cantidadBebida} bebidas"