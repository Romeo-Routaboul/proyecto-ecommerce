from django.db import models

# Create your models here.

class Usuario(models.Model):
    username = models.CharField(max_length=50, unique=True)
    nombre_completo = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=80)

class Categoria(models.Model):
    descripcion = models.CharField(max_length=100)

class Item(models.Moddel):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
