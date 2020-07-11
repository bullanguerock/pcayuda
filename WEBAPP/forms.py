from django.forms import ModelForm, TextInput, EmailInput, EmailField
from .models import Cliente, Contacto
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .widgets import CustomPhoneNumberPrefixWidget

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
        #error_messages = {'invalid': 'This is my email error msg.'}
        #mail = forms.EmailField(error_messages={'invalid': 'This is my email error msg.'}, 
        #widget=forms.EmailInput(attrs={'class':'form-control-input', 'autocomplete':'off'}), 
        #required=True)
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control-input'}),
            'last_name': TextInput(attrs={'class': 'form-control-input'}),
            'mail': EmailInput(attrs={'class': 'form-control-input', 'autocomplete':'off'}),
            'phone': CustomPhoneNumberPrefixWidget(initial=('+56', 'Chile +56'), attrs={'class': 'form-control-input'}),
            'pay_method': TextInput(attrs={'class': 'form-control-input'}),
            }

class AddressForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['region', 'comuna', 'address']

