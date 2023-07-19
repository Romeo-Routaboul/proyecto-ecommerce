from django.urls import path
from core.views import*

urlpatterns = [
#path("", inicio, name="inicio"),
path("signup/", SignUpView.as_view(), name="signup"),
path("inicio/", inicio, name="inicio"),
path("resultado/", resultado_busqueda_productos, name="resultado"),

]

# esto es un cambio