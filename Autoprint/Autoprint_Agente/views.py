from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Autoprint_API.models import Documento, Cliente,Impressao, Agente, Pedido

# Create your views here.
@login_required
def pedidosDoAgente(request):
    agent = Agente.objects.get(user_id = request.user.id)
    pedidos = Pedido.objects.filter(id_agent=agent.id)
    pedidoswithdocs = list()
    for p in pedidos:
        impreped = Impressao.objects.filter(id_client=p.id_client.id,pedido=p.id)
        docs = ""
        if(impreped):
            for i in impreped:
                docs+=(i.id_document.file.name.split('/')[1])+" | "
            pedidoswithdocs.append((p,docs))
    response =render(request,'pedidoslistagent.html',{"user":request.user,
                                                  "pedidos":pedidoswithdocs
                                                     })
    return response