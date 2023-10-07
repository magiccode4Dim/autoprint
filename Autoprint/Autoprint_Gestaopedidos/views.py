from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Autoprint_API.models import Documento, Cliente,Impressao
import os
from django.utils.datastructures import MultiValueDictKeyError


USER_WEB_PATH = "/user/"
GESTIN_WEB_PATH = "/impressoes/"

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
    response =render(request,'uploadeddocs.html',{"user":request.user,
                                                  "documents":documents
                                                     })
    return response

#adicionar uma impressao
@method_decorator(login_required, name='dispatch')
class adicionarImpressao(View):
    def get(self, request, *args, **kwargs):
        cli = Cliente.objects.get(user_id = request.user.id)
        documents = Documento.objects.filter(id_client=cli.id)
        response =render(request,'createimpressao.html',{"user":request.user,
                                                         "documents":documents
                                                })
        return response
    def post(self, request, *args, **kwargs):
        if len(request.POST.get("docid")) == 0:return redirect(GESTIN_WEB_PATH+"uploaddocumet/")
        docid = request.POST.get("docid")
        cli = Cliente.objects.get(user_id = request.user.id)
        doc = Documento.objects.get(id=docid)
        newi = Impressao()
        newi.id_client = cli
        newi.id_document = doc
        newi.save()
        return redirect(GESTIN_WEB_PATH+"minhasimpressoes/")

#ver lista de impressoes existentes
@login_required
def impressoesCriadas(request):
    cli = Cliente.objects.get(user_id = request.user.id)
    impressoes = Impressao.objects.filter(id_client=cli.id)
    response =render(request,'impressoeslist.html',{"user":request.user,
                                                  "impressoes":impressoes
                                                     })
    return response
