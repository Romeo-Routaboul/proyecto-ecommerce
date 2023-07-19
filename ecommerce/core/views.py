from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from core.models import*
from core.forms import*

from .forms import MyUserCreationForm

# Create your views here.

#def inicio(request):
#  return render (request, "core/index.html")

class SignUpView(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def inicio(request):
    return render (request, "core/index.html")


def resultado_busqueda_productos(request):
    nombre_item = request.GET["nombre_item"]

    resultados = Item.objects.filter(nombre__icontains = nombre_item)
    return render (request, "core/resultado-busqueda.html", {"resultados": resultados})
