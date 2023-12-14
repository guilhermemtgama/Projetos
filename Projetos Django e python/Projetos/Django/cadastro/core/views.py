from django.shortcuts import render
from core.models import Funcionarios

# Create your views here.

def lista_cadastro(request):
   funcionarios = Funcionarios.objects.all()
   dados = {'funcionarios': funcionarios}
   return render(request, 'cadastro.html', dados)
