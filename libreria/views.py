from django.shortcuts import render, redirect
from django.views import View
from .forms import LibreriaForm
from .models import Libreria
"""
class Formulario(View):
    Libreria_template = 'Libreria/listado.html'

    def get(self,request):
        form = LibreriaForm()
        return render(request, self.Libreria_template, {'form': form})
    
    def post(self,request):
        form = LibreriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmacion')
        return render(request, self.Libreria_template, {'form': form})

class Confirmacion(View):
    confirmacion_template = 'Libreria/confirmacion.html'

    def get(self,request):
        return render(request, self.confirmacion_template)

class Lista_Libreria(View):
    lista_Libreria_template = 'Libreria/lista_Libreria.html'

    def get(self,request):
        Libreria = Libreria.objects.all()
        return render(request, self.lista_Libreria_template, {'Libreria': Libreria})
"""