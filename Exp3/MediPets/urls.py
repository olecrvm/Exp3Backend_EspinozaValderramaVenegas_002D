from django.urls import path
from .views import index, index2, index3, index4,Ver, form_mascota, form_modificar, form_eliminar

urlpatterns=[
    path('', index, name="index"),
    path('index2', index2, name="galeria"),
    path('index3', index3, name="nosotros"),
    path('index4', index4, name="iniciosesion"),
    path('ver', Ver, name="ver"),
    path('Form_crearmascota', form_mascota, name="crear"),
    path('form_ModMascota/<id>', form_modificar, name="Modificar"),
    path('form_EliminarMascota/<id>', form_eliminar, name="Eliminar") 
]