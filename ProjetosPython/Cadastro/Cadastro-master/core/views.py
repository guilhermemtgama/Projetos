from django.shortcuts import render, redirect
from core.models import Cadastro
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime
from django.http.response import Http404
# Create your views here.

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario= authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, " Usuário ou senha inválido")

    return redirect('/')

@login_required(login_url='/login/')
def lista_casdastro(request):
    usuario = request.user
    cadastro = Cadastro.objects.filter(usuario=usuario)
    dados = {'cadastros': cadastro}
    return render(request, 'cadastro.html', dados)

@login_required(login_url='/login/')
def funcionario(request):
    id_funcionario = request.GET.get('id')
    dados = {}
    if id_funcionario:
        dados['funcionario'] = Cadastro.objects.get(id=id_funcionario)
    return render(request, 'funcionario.html', dados)

@login_required(login_url='/login/')
def submit_cadastro(request):
    if request.POST:
        Nome     = request.POST.get('Nome')
        Idade    = request.POST.get('Idade')
        Telefone = request.POST.get('Telefone')
        usuario  = request.user
        id_funcionario = request.POST.get('id_funcionario')
        if id_funcionario:
            Cadastro.objects.filter(id=id_funcionario).update(Nome = Nome,
                                                              Idade = Idade,
                                                              Telefone = Telefone)
        else:
            Cadastro.objects.create(Nome = Nome,
                                    Idade = Idade,
                                    Telefone = Telefone,
                                    usuario =usuario)
    return redirect('/')


@login_required(login_url='/login/')
def delete_cadastro(request, id_cadastro):
    usuario = request.user
    try:
        cadastro =Cadastro.objects.get(id=id_cadastro)
    except Exception:
        raise Http404()
    if usuario==cadastro.usuario:
        cadastro.delete()
    else:
        raise Http404()
    return redirect('/')

