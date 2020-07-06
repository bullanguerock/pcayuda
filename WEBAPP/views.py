from django.shortcuts import render
from django.http import JsonResponse
from dashboard.models import Order
from django.core import serializers
from .forms import CustomerForm
from .models import Cliente

# Create your views here.
def index(request):
    return render(request,'WEBAPP/index.html')

def terms(request):
    return render(request,'WEBAPP/terms-conditions.html')

def policy(request):
    return render(request,'WEBAPP/privacy-policy.html')

def add_client(request):
    fname = request.POST["fname"]
    lname = request.POST["lname"]
    presu = request.POST["presu"]
    email = request.POST["email"]
    phone = request.POST["phone"]
    service = request.POST["service"]
    pay_method = request.POST["pay_method"]
    necesity = request.POST["necesity"]


    cliente = Cliente(first_name = fname, last_name = lname, mail = email,
                phone = phone, presu = presu, necesity = necesity, pay_method = pay_method,
                status = 'pendiente', service = service)
    cliente.save()


    return render(request,'WEBAPP/new_client.html')