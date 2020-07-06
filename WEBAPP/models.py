from django.db import models

# Create your models here.

class Cliente(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    presu = models.CharField(max_length=50)
    necesity = models.TextField(max_length=300)
    service = models.CharField(max_length=50)
    pay_method= models.CharField(max_length=50)
    date_register = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return (self.first_name + ' ' + self.last_name)

class Direccion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    reigion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    address = models.CharField(max_length=100)