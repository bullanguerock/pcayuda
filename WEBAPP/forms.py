from django.forms import ModelForm, TextInput
from .models import Cliente, Contacto
from django import forms

class CustomerForm(ModelForm):
    class Meta:
        model = Cliente
        service = forms.ChoiceField(choices=Cliente.SERVICE_CHOICES)
        fields = ['presu', 'service']        
        widgets = {

        }

class NbForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['necesity']
        widgets = {
            'necesity': TextInput(attrs={'class': 'form-control-textarea'}),
            }
class ContactForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['first_name', 'last_name', 'mail', 'phone','pay_method']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control-input'}),
            'last_name': TextInput(attrs={'class': 'form-control-input'}),
            'mail': TextInput(attrs={'class': 'form-control-input'}),
            'phone': TextInput(attrs={'class': 'form-control-input'}),
            'pay_method': TextInput(attrs={'class': 'form-control-input'}),
            }

class AddressForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['region', 'comuna', 'address']

