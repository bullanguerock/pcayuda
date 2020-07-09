from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from dashboard.models import Order
from django.core import serializers
from .forms import CustomerForm, NbForm, ContactForm
from .models import Cliente

# Create your views here.
def index(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return redirect('form2', pk=cliente.pk)
    else:
        form = CustomerForm()
    return render(request,'WEBAPP/index.html')
    

def terms(request):
    return render(request,'WEBAPP/terms-conditions.html')

def policy(request):
    return render(request,'WEBAPP/privacy-policy.html')

def formtest(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return redirect('form2', pk=cliente.pk)
    else:
        form = CustomerForm()
    return render(request, 'WEBAPP/formtest.html', {'form': form})

def form2(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form2 = NbForm(request.POST , instance=cliente)
        if form2.is_valid():
            cliente = form2.save(commit=False)
            cliente.save()
            return redirect('form3', pk=cliente.pk)
    else:
        form2 = NbForm()
    return render(request, 'WEBAPP/form2.html', {'form2': form2})

def form3(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form3 = ContactForm(request.POST , instance=cliente)
        if form3.is_valid():
            cliente.status = 'pendiente'
            cliente = form3.save(commit=False)
            cliente.save()
            return redirect('new_client', pk=cliente.pk)
    else:
        form3 = ContactForm()
    return render(request, 'WEBAPP/form3.html', {'form3': form3})

def new_client(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    name = cliente.first_name +' '+ cliente.last_name
    return render(request,'WEBAPP/new_client.html', {'name': name})


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

def slider(request):  
    return render(request,'WEBAPP/slider.html')
