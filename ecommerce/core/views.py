from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import MyUserCreationForm

# Create your views here.

#def inicio(request):
#  return render (request, "core/index.html")

class SignUpView(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'