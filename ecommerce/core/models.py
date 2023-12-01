from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Categoria(models.Model):
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return self.descripcion

class Item(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="fotos", null=True, blank=True)

    def __str__(self):
        return self.nombre
    
class Carrito (models.Model):
    #user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)



class MyUser(AbstractUser):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=40)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, null=True)
