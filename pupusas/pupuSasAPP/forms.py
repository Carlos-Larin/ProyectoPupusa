from django import forms
from . import models

class createPost(forms.ModelForm):
    class Meta:
        model = models.pagoPupas
        fields = ['cantidadPupusas',
                  'tipoDePupusa',
                  'cantidadBebida',
                  'tipoDeBebida',
                  'correoCliente',
                  'pagaCon']
        db_table = ''
        managed = True
        verbose_name = ':'
        verbose_name_plural = ':s'