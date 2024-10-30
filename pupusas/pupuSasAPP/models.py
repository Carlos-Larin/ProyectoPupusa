from django.db import models

# Create your models here.
class pagoPupas(models.Model):
    cantidadPupusas= models.IntegerField()
    cantidadBebida= models.IntegerField()
    correoCliente= models.EmailField(max_length=200)
    pagaCon = models.DecimalField(max_digits=10, decimal_places=4)
