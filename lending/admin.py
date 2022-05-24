from django.contrib import admin

from lending.models import Lending

# Register your models here.
@admin.register(Lending)
class LendingAdmin(admin.ModelAdmin):

    field = '__all__'
