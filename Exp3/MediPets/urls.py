from django.urls import path
from .views import index, index2, index3, index4

urlpatterns=[
    path('', index, name="index"),
    path('index2', index2, name="galeria"),
    path('index3', index3, name="nosotros"),
    path('index4', index4, name="iniciosesion"),
]