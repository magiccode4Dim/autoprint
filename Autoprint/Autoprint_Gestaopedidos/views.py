from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Autoprint_API.models import Documento, Cliente,Impressao, Agente, Pedido
import os
from django.utils.datastructures import MultiValueDictKeyError
from django.utils import timezone
import random
from django.conf import settings

#retorna um numero de confirmacao aleatorio
def get_randomid():
    numero_aleatorio = random.randint(100000, 999999)
    return numero_aleatorio

USER_WEB_PATH = "/user/"
GESTIN_WEB_PATH = "/impressoes/"
AGENT_WEB_PATH = "/agent/"
API_WEB_PATH = "/api/"

#Verifica se o arquivo é permitido
def is_valid_file_type(file):
    file_extension = os.path.splitext(file.name)[1].lower()
    valid_extensions = ['.pdf', '.docx']
    return file_extension in valid_extensions

#fazer upload de um documento
@method_decorator(login_required, name='dispatch')
class carregarDocumentos(View):
    def get(self, request, *args, **kwargs):
        response =render(request,'uploadfile.html',{"user":request.user
                                                })
        return response
    def post(self, request, *args, **kwargs):
        try:
            request.FILES['file']
        except MultiValueDictKeyError as e:
            return redirect(GESTIN_WEB_PATH+"uploaddocumet/")
        arquivo = request.FILES['file']
        if not is_valid_file_type(arquivo):
            #se o arquivo nao for valido
            return redirect(GESTIN_WEB_PATH+"uploaddocumet/")
        doc =  Documento()
        doc.id_client = Cliente.objects.get(user_id = request.user.id)
        doc.file.save(arquivo.name, arquivo)
        doc.save()
        return redirect(GESTIN_WEB_PATH+"uploadeddocumets/")
        
#ver lista de documentos carregados        
@login_required
def documentosCarregados(request):
    cli = Cliente.objects.get(user_id = request.user.id)
    documents = Documento.objects.filter(id_client=cli.id)
    docwithoutDocc = list()
    for d in documents:
        #remove a barra
        docwithoutDocc.append((d,d.file.name.split('/')[1]))
    response =render(request,'uploadeddocs.html',{"user":request.user,
                                                  "documents":docwithoutDocc
                                                     })
    return response

#adicionar uma impressao
@method_decorator(login_required, name='dispatch')
class adicionarImpressao(View):
    def get(self, request,documento, *args, **kwargs):
        agents = Agente.objects.all()
        doc = Documento.objects.get(file="DOCUMENTOS/"+documento)        
        response =render(request,'createimpressao.html',{"user":request.user,
                                                         "documentname":documento,
                                                         "agents":agents,
                                                         "doc":doc  
                                                })
        return response
    def post(self, request, *args, **kwargs):
        #cria a impressao
        if len(request.POST.get("docid")) == 0:return redirect(GESTIN_WEB_PATH+"uploaddocumet/")
        docid = request.POST.get("docid")
        cli = Cliente.objects.get(user_id = request.user.id)
        doc = Documento.objects.get(id=docid)
        newi = Impressao()
        newi.id_client = cli
        newi.id_document = doc
        #cria o pedido
        if len(request.POST.get("agentid")) == 0:
            #apaga a impressao
            return redirect(GESTIN_WEB_PATH+"uploaddocumet/")
        newi.save()
        #preecher dados do agente
        agentid = request.POST.get("agentid")
        cli = Cliente.objects.get(user_id = request.user.id)
        agent = Agente.objects.get(id = agentid)
        ped = Pedido()
        ped.id_client= cli
        ped.id_agent=agent
        r1 =get_randomid()
        r2=get_randomid()
        ped.idConf_inpre=r1
        ped.idConf_cli=r2
        ped.save()
        pedobj = Pedido.objects.get(id_client = cli.id, id_agent = agent.id,idConf_inpre=r1,idConf_cli=r2)
        impressoes = Impressao.objects.filter(id_client=cli.id, pedido=-1, id_document=doc.id)
        impressoes.update(pedido= pedobj.id)
        return redirect(GESTIN_WEB_PATH+"pedidoscriados/")

#ver lista de impressoes existentes
"""@login_required
def impressoesCriadas(request):
    cli = Cliente.objects.get(user_id = request.user.id)
    impressoes = Impressao.objects.filter(id_client=cli.id)
    response =render(request,'impressoeslist.html',{"user":request.user,
                                                  "impressoes":impressoes
                                                     })
    return response

#criar pedido de impressao
@method_decorator(login_required, name='dispatch')
class criarPedidoImpressao(View):
    def get(self, request, *args, **kwargs):
        cli = Cliente.objects.get(user_id = request.user.id)
        impressoes = Impressao.objects.filter(id_client=cli.id)
        agents = Agente.objects.all()
        response =render(request,'createpedido.html',{"user":request.user,
                                                         "impressoes":impressoes,
                                                         "agents":agents                             
                                                })
        return response
    def post(self, request, *args, **kwargs):
        if len(request.POST.get("agentid")) == 0:return redirect(GESTIN_WEB_PATH+"criarpedidoimpressao/")
        #preecher dados do agente
        agentid = request.POST.get("agentid")
        cli = Cliente.objects.get(user_id = request.user.id)
        agent = Agente.objects.get(id = agentid)
        ped = Pedido()
        ped.id_client= cli
        ped.id_agent=agent
        r1 =get_randomid()
        r2=get_randomid()
        ped.idConf_inpre=r1
        ped.idConf_cli=r2
        ped.save()
        pedobj = Pedido.objects.get(id_client = cli.id, id_agent = agent.id,idConf_inpre=r1,idConf_cli=r2)
        #marcar as impressoes com o id do novo pedido
        impressoes = Impressao.objects.filter(id_client=cli.id)
        for i in impressoes:
            if "in_"+str(i.id) in request.POST:
                if i.pedido == -1:
                    inpre = Impressao.objects.filter(id=i.id, id_client=cli.id)
                    if inpre:
                        inpre.update(pedido = pedobj.id)
                
        return redirect(GESTIN_WEB_PATH+"pedidoscriados/")"""
 
 #ver pedidos 
@login_required
def pedidosCriados(request):
    cli = Cliente.objects.get(user_id = request.user.id)
    pedidos = Pedido.objects.filter(id_client=cli.id)
    pedidoswithdocs = list()
    for p in pedidos:
        impreped = Impressao.objects.filter(id_client=cli.id,pedido=p.id)
        docs = ""
        if(impreped):
            for i in impreped:
                docs+=(i.id_document.file.name.split('/')[1])+" | "
            pedidoswithdocs.append((p,docs))
                
                
    

    response =render(request,'pedidoslist.html',{"user":request.user,
                                                  "pedidos":pedidoswithdocs
                                                     })
    return response

#confirmar pedido
@method_decorator(login_required, name='dispatch')
class confirmarPedido(View):
    def get(self, request, *args, **kwargs):
        try:
            agent = Agente.objects.get(user_id = request.user.id)
        except Exception as e:
            return JsonResponse({"Erro":"Acesso Negado"})
        response =render(request,'confirmarpedido.html',{"user":request.user
                                                })
        return response
    def post(self, request, *args, **kwargs):
        if len(request.POST.get("ccped")) == 0:return redirect(GESTIN_WEB_PATH+"confirmarpedido/")
        agent = Agente.objects.get(user_id = request.user.id)
        pedidos = Pedido.objects.filter(id_agent=agent.id,idConf_cli=int(request.POST.get("ccped")))
        if pedidos:
            pedidos.update(isconfirmed=True,data_conclusao=timezone.now().strftime('%Y-%m-%d'))
        else:
            return redirect(GESTIN_WEB_PATH+"confirmarpedido/") 
        inp = Impressao.objects.get(pedido=pedidos.first().id)
        doc = Documento.objects.get(id=inp.id_document.id)
        return redirect(AGENT_WEB_PATH+"viewpdfforprint?file="+doc.file.name.split("/")[1]+"&ccc="+request.POST.get("ccped"))
    
#apagar pedido
@login_required
def apagarPedido(request,id):
    cli = Cliente.objects.get(user_id = request.user.id)
    pedido = Pedido.objects.get(id=id, id_client=cli.id)
    pedido.delete()
    return redirect(GESTIN_WEB_PATH+"pedidoscriados/")

#apagar documento
@login_required
def apagarDocumento(request,id):
    cli = Cliente.objects.get(user_id = request.user.id)
    docu = Documento.objects.get(id=id, id_client=cli.id)
    if(docu):
        caminho_arquivo = os.path.join(settings.MEDIA_ROOT, str(docu.file))
        if os.path.exists(caminho_arquivo):
                # Remove o arquivo do sistema de arquivos
                os.remove(caminho_arquivo)
                docu.delete()
    return redirect(GESTIN_WEB_PATH+"uploadeddocumets/")

#baixar documento
@login_required
def baixarDocumento(request,id):
    cli = Cliente.objects.get(user_id = request.user.id)
    docu = Documento.objects.get(id=id, id_client=cli.id)
    if(docu):
        caminho_arquivo = os.path.join(settings.MEDIA_ROOT, str(docu.file))
        if os.path.exists(caminho_arquivo):
            filename = docu.file.name.split("/")[1]
            return redirect(API_WEB_PATH+f"downloadfile/{filename}")
    return JsonResponse({"error":"permissao negada"})
