from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from core.models import*
from core.forms import*
from django.views.generic import DetailView

from .forms import MyUserCreationForm

# Create your views here.

#def inicio(request):
#  return render (request, "core/index.html")

class SignUpView(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def inicio(request):
    productos = Item.objects.all
    return render (request, "core/index.html", {"productos": productos})


def resultado_busqueda_productos(request):
    nombre_item = request.GET["nombre_item"]

    resultados = Item.objects.filter(nombre__icontains = nombre_item)
    return render (request, "core/resultado-busqueda.html", {"resultados": resultados})

class ItemDetail(DetailView):
    model = Item
    template_name = "core/detail_item.html"