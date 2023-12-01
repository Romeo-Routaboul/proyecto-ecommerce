from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from core.models import *
from core.forms import *
from django.views.generic import DetailView
from django.contrib.auth import authenticate, login
from .forms import MyUserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required


class SignUpView(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

@login_required
def inicio(request):
    productos = Item.objects.all()

    return render (request, "core/index.html", {"productos": productos})


def resultado_busqueda_productos(request):
    nombre_item = request.GET["nombre_item"]
    if len(nombre_item) >= 1:
        resultados = Item.objects.filter(nombre__icontains = nombre_item)
        return render (request, "core/resultado-busqueda.html", {"resultados": resultados})
    else:
        return render (request, "core/resultado-busqueda.html", {"resultados": []})

class ItemDetail(DetailView):
    model = Item
    template_name = "core/detail_item.html"

def carrito(request):
    
    return render (request, "core/carrito.html")


def iniciar_sesion (request):

    errors = ""

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username=data["username"], password=data["password"])

            if user is not None:
                login (request, user)
                return redirect("inicio")
            else:
                return render (request, "core/login.html", {"form": formulario, "errors": "credenciales invalidas"})

        else:
            return render(request, "core/login.html", {"form": formulario, "errors": formulario.errors})

    formulario = AuthenticationForm()
    return render (request , "core/login.html", {"form":formulario, "errors": errors})

def registrarse (request):

    if request.method == "POST":
        formulario = MyUserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect ("signup-exitoso")
        else:
            return render (request, "core/signup.html", {"form": formulario, "errors": formulario.errors})

    formulario = MyUserCreationForm()
    return render (request, "core/signup.html", {"form": formulario})

def signup_finalizado(request):
    return render (request, "core/signup_exitoso.html")



























