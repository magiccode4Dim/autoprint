from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,JsonResponse,FileResponse
import json
from django.middleware.csrf import get_token
from django.contrib.auth.decorators import login_required
from django.templatetags.static import static
import os
from django.conf import settings
from Autoprint_API.models import Documento, Cliente,Impressao, Agente, Pedido
from urllib.parse import quote
from django.views.decorators.clickjacking import xframe_options_exempt
from Autoprint_Gestaopedidos.views import get_randomid
from django.core.serializers import serialize
import json
from django.contrib.auth.models import User

# Create your views here.

@login_required
def downloadFiles(request,ficheiro):
    ficheiro = "DOCUMENTOS/"+ficheiro
    try:
        cli = Cliente.objects.get(user_id = request.user.id)
        document =  Documento.objects.filter(id_client=cli.id, file=ficheiro).first()
    except Exception as e:
        try:
            #deve ter um parametro adicional como, precisa do CCC do cliente
            ccc = request.GET.get("ccc")
            agent = Agente.objects.get(user_id = request.user.id)
            pedido = Pedido.objects.get(id_agent=agent.id, idConf_cli=ccc)
            document =  Documento.objects.filter(file=ficheiro).first()
            impre = Impressao.objects.get(pedido=pedido.id,id_document=document.id)
            if(impre==None):return JsonResponse({"erro":"Sem permissao1"})
            #Por questoes de seguranca o CCC é actualizado sempre que o agente vizualiza o documento
            #isso quer dizer que nao é possivel vizualizar duas vezes com o mesmo CCC
            #Pedido.objects.filter(id_agent=agent.id,idConf_cli=int(ccc)).update(idConf_cli=get_randomid())
        except Exception as e:
            return JsonResponse({"erro":"Sem permissao2"+str(e)})
        #permitir o agente baixar os pdfs dos seus pedidos;; 
    if(document==None):
        return JsonResponse({"erro":"Sem permissao"})
    caminho_arquivo = os.path.join(settings.MEDIA_ROOT, ficheiro)
    if os.path.exists(caminho_arquivo):
                file = open(caminho_arquivo, 'rb')
                response = FileResponse(file)
                response['Content-Disposition'] = f'attachment; filename="{os.path.basename(caminho_arquivo)}"'
                #file.close()
                return response
    else:
        return JsonResponse({"erro":"404 documento nao encontrado"})
    
    
@login_required
@xframe_options_exempt
def readpdf(request,pdfname):
    response = render(request,"viewpdf.html")
    response.set_cookie('documentname', quote(pdfname))
    return response

#AGENTE
#Retorna uma lista com os pedidos do agente
@login_required
def pedidosDoAgenteJson(request):
    agent = Agente.objects.get(user_id = request.user.id)
    pedidos = Pedido.objects.filter(id_agent=agent.id)
    pedidoswithdocs = list()
    for p in pedidos:
        impreped = Impressao.objects.filter(id_client=p.id_client.id,pedido=p.id)
        docs = ""
        if(impreped):
            for i in impreped:
                docs+=(i.id_document.file.name.split('/')[1])+" | "
            pedidoJson = json.loads(serialize('json', [p]))[0]
            pedidoJson["documentName"] =  docs
            clientJson = json.loads(serialize('json', [Cliente.objects.get(id=(pedidoJson["fields"])["id_client"])]))[0]
            userJson = json.loads(serialize('json', [User.objects.get(id=(clientJson["fields"])["user"])]))[0]
            pedidoJson["clientusername"]=   (userJson["fields"])["username"]
            pedidoswithdocs.append(pedidoJson)

    return JsonResponse(pedidoswithdocs, safe=False) #assim eu devo tomar cuidado com os dados que sao enviados nesse response porque o safe esta falso