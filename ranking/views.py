# -*- coding: utf-8 -*-
from atento.cliente.models import *
from atento.cliente.forms import *
from django.shortcuts import render_to_response
 
def list(request):
    list = login_required(list)
    clienteform = ClienteForm()
    clientes = Cliente.objects.all()
    bairros = Bairro.objects.all()
return render_to_response('clienteform.html',{
    'form':clienteform,
    'clientes':clientes,
    'bairros':bairros,
    'operacao':'Cadastrar',
  })# Create your views here.
  
  
from django.http import HttpResponse
def add(request):
  if request.method == 'POST':
    clienteform = ClienteForm(request.POST)
    if clienteform.is_valid():
      clienteform.save()
      mensagem = 'Cadastro realizado com sucesso.'
    else:
      mensagem = 'Erro na validacao do form.'
 
    clientes = Cliente.objects.all()
    operacao = 'Cadastrar'
    return render_to_response('clienteform.html',{'form':clienteform, 'clientes':clientes, 'mensagem':mensagem, 'operacao':operacao})
  else:
    return HttpResponse("Nao foi submetido nenhum formulario.")
def edit(request):
   if request.method == 'POST':
    id = request.POST.get('listaclientes')
   if id > 0:
      clientes = Cliente.objects.get(pk=id)      
      clienteform = ClienteForm(instance=clientes)
      form_url = '/cliente/update/'
      operacao = 'Atualizar'
return render_to_response('clientes.html' {'form':clienteform, 'id_cliente':id, 'form_url':form_url, 'operacao':operacao})
    else:
      return HttpResponse("Nenhum cliente foi selecionado. id=0.")
     else:
      return HttpResponse("Nao foi submetido nenhum formulario.")

def update(request):
  if request.method == 'POST':
    id = request.POST.get('id')
    if id > 0:
      cliente = Cliente.objects.get(pk=id)
      clienteform = ClienteForm(request.POST,instance=cliente)
      if clienteform.is_valid():
        clienteform.save()
        return HttpResponseRedirect('/cliente/list/')
      else:
        mensagem = 'erro'
        operacao = 'Atualizar'
        return render_to_response('clienteform.html',{'form':clienteform, 'mensagem':mensagem, 'id_cliente':id, 'operacao':operacao})
 
    else:
      return HttpResponse("Nenhum cliente foi selecionado. id=0.")
  else:
    return HttpResponse("Nao foi submetido nenhum formulario.")

def search(request):
  if request.method == 'POST':
    palavra = request.POST.get('busca')
    if len(palavra) > 0:
      from django.db.models import Q
      clientes = Cliente.objects.filter(Q(nome__icontains=palavra) | Q(cpf__icontains=palavra))
      bairros = Bairro.objects.all()
      clienteform = ClienteForm()
      return render_to_response('clienteform.html',{
        'form':clienteform,
        'clientes':clientes,
        'bairros':bairros,
        'operacao':'Cadastrar',
        'titulo':'RESULTADO DA BUSCA'
      })
    else:
      return HttpResponse("Nao foi digitado nada no campo de busca.")
  else:
      return HttpResponse("O formulario nao foi submetido.")
  
from django.contrib.auth.decorators import login_required
def welcome(request):
  return HttpResponse('Bem-vindo! Voce esta logado no sistema.')
welcome = login_required(welcome)


