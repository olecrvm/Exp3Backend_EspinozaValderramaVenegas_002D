from django.db import models

# Create your models here.

class TipoMascota(models.Model):
    idTipo=models.IntegerField(primary_key=True, verbose_name='Id de Tipo de Mascota: ')
    nomTipo=models.CharField(max_length=50, verbose_name='Nombre del Tipo de Mascota: ')

    def __str__(self):
        return(self.nomTipo)

class Mascota(models.Model):
    nroChip=models.CharField(primary_key=True, max_length=6, verbose_name='Numero de Chip: ')
    nombre=models.CharField(max_length=30, verbose_name='Nombre de la Mascota: ')
    dueno=models.CharField(max_length=30, verbose_name='Nombre del dueño de la Mascota: ')
    tipo=models.ForeignKey(TipoMascota, on_delete=models.CASCADE)

    def __str__(self):
        return(self.nroChip)