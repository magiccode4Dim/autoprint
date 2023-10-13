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