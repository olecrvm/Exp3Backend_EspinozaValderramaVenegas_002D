from django.shortcuts import render, redirect
from .models import Mascota
from .forms import mascotaForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def index2(request):
    return render(request, 'index2.html')

def index3(request):
    return render(request, 'index3.html')

def index4(request):
    return render(request, 'index4.html')

def form_mascota(request):
   if request.method=='POST':
          mascota_form = mascotaForm(request.POST)
          if mascota_form.is_valid():
             mascota_form.save()
             return redirect('index')
   else:
        mascota_form=mascotaForm()    
   return render(request, 'MediPets/Form_crearmascota.html', {'mascota_form':mascota_form})

def Ver(request):
    mascotas = Mascota.objects.all()
    return render(request, 'MediPets/Ver.html', context={'usuarios':mascotas})

def form_modificar(request,id):
    mascota = Mascota.objects.get(nroChip=id)

    datos ={
        'form': mascotaForm(instance=mascota)
    }
    if request.method == 'POST': 
        formulario = mascotaForm(data=request.POST, instance = mascota)
        if formulario.is_valid: 
            formulario.save()
            return redirect('ver')
    return render(request, 'MediPets/Form_ModMascota.html', datos)

def form_eliminar(request,id):
    mascota = Mascota.objects.get(nroChip=id)
    mascota.delete()
    return redirect('ver')