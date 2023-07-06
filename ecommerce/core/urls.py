from django.urls import path
from core.views import*

urlpatterns = [
#path("", inicio, name="inicio"),
path("signup/", SignUpView.as_view(), name="signup"),

]