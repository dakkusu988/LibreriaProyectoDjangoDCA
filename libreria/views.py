from django.shortcuts import render, redirect
from django.views import View
from .forms import LibreriaForm
from .models import Libreria
from django.views.generic import ListView, DetailView

"""
class Listado(View):
    libreria_template = 'libreria/listado.html'

    def get(self,request):
        libros = Libreria.objects.all()
        return render(request, self.libreria_template, {'libros': libros})
"""
class Listado(View):
    model = Libreria
    template_name = 'libreria/listado.html'

    
class Añadir(View):
    libreria_template = 'libreria/añadir.html'

    def get(self,request):
        form = LibreriaForm()
        return render(request, self.libreria_template, {'form': form})

    def post(self,request):
        form = LibreriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado')
        return render(request, self.libreria_template, {'form': form})

class Detalles(View):"""
    libreria_template = 'libreria/detalles.html'

    def get(self,request):
        return render(request, self.libreria_template)

"""
class Editar(View):"""
    libreria_template = 'libreria/editar.html'

    def get(self,request):
        libreria = Libreria.objects.all()
        return render(request, self.libreria_template, {'libreria': libreria})"""