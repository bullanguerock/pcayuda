from django.contrib import admin
from .models import Cliente
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cliente._meta.fields if field.name != "id"]
admin.site.register(Cliente, ClienteAdmin)


