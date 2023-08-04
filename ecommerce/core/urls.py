from django.urls import path
import ecommerce.settings as settings
from django.conf.urls.static import static

from core.views import SignUpView, ItemDetail, resultado_busqueda_productos, inicio

urlpatterns = [
#path("", inicio, name="inicio"),
path("signup/", SignUpView.as_view(), name="signup"),
path("inicio/", inicio, name="inicio"),
path("resultado/", resultado_busqueda_productos, name="resultado"),
path("detail/<pk>/", ItemDetail.as_view() , name="detail"),

]
