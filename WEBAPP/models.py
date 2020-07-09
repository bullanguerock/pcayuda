from django.db import models
from django import forms

# Create your models here.


class Cliente(models.Model):
    SERVICE_CHOICES = [('Notebooks'), ('Computadores Escritorio'),('Piezas/Componentes')]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    presu = models.CharField(max_length=50)
    service = models.CharField(max_length=50)
    necesity = models.TextField(max_length=300)
    pay_method= models.CharField(max_length=50)
    date_register = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return (self.first_name + ' ' + self.last_name)

class Contacto(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    region = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class Cotizacion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    file = models.CharField(max_length=100)
    date_register = models.DateTimeField(auto_now_add=True)
