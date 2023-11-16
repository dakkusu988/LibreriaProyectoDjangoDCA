# Archivo urls.py de libreria

from django.urls import path
from .views import Listado, Detalles, Editar, Añadir

urlpatterns = [
    path('', Listado.as_view(), name='listado'),
    path('detalles/', Detalles.as_view(), name='detalles'),
    path('editar/', Editar.as_view(), name='editar'),
    path('añadir/', Añadir.as_view(), name='añadir'),
]