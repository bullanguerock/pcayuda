from django.forms import ModelForm
from .models import Cliente

class CustomerForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['first_name', 'last_name', 'mail', 'phone', 'presu',
                    'necesity', 'pay_method']