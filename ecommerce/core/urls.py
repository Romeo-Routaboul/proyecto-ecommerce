from django.urls import path
import ecommerce.settings as settings
from django.conf.urls.static import static

from core.views import ItemDetail, resultado_busqueda_productos, inicio, carrito, iniciar_sesion, registrarse

urlpatterns = [
path("", iniciar_sesion, name="login"),
path("inicio/", inicio, name="inicio"),
path("resultado/", resultado_busqueda_productos, name="resultado"),
path("detail/<pk>/", ItemDetail.as_view() , name="detail"),
path("carrito/", carrito , name="carrito"),
path("signup/", registrarse , name= "signup")


]
