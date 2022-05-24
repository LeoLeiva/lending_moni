from dataclasses import fields
from django.contrib import admin

from client.models import ClientModel

# Register your models here.
@admin.register(ClientModel)
class ClientAdmin(admin.ModelAdmin):

    field = '__all__'
