from django.contrib import admin
from core.models import Funcionarios

# Register your models here.

class FuncionariosAdmin (admin.ModelAdmin):
    list_display = ('Nome', 'Idade', 'Telefone')



admin.site.register(Funcionarios, FuncionariosAdmin)