from django import forms 
from django.forms import ModelForm, widgets
from .models import Mascota


class mascotaForm(ModelForm):
    
    class Meta:
        model= Mascota
        fields = ['nroChip', 'nombre', 'dueno', 'tipo']
        labels ={
            'nroChip':'Ingrese número del chip',
            'nombre': ' Ingrese nombre de la mascota',
            'dueno': '  Ingrese nombre del dueño',
            'tipo': '   indique tipo de mascota'

        }
        widgets={
            'nroChip': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Número de Chip',
                    'id': 'nroChip'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Nombre de la mascota',
                    'id': 'nombre'
                }
            ),
            'dueno': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Nombre del dueño',
                    'id': 'dueno'
                }
            ),
            'nomTipo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Tipo de mascota',
                    'id': 'tipo'
                }
            )
        }