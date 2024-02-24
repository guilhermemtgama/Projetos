from django.contrib import admin
from core.models import Cadastro

# Register your models here.

class cadastroadmin(admin.ModelAdmin):
    list_display = ('id','Nome', 'Idade', 'Telefone')

admin.site.register(Cadastro, cadastroadmin)
