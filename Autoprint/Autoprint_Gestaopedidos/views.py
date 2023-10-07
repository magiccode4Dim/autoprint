from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Autoprint_API.models import Documento, Cliente
import os

USER_WEB_PATH = "/user/"
GESTIN_WEB_PATH = "/impressoes/"

#Verifica se o arquivo é permitido
def is_valid_file_type(file):
    file_extension = os.path.splitext(file.name)[1].lower()
    valid_extensions = ['.pdf', '.docx']
    return file_extension in valid_extensions


@method_decorator(login_required, name='dispatch')
class carregarDocumentos(View):
    def get(self, request, *args, **kwargs):
        response =render(request,'uploadfile.html',{"user":request.user
                                                })
        return response
    def post(self, request, *args, **kwargs):
        arquivo = request.FILES['file']
        if not is_valid_file_type(arquivo):
            #se o arquivo nao for valido
            return redirect(GESTIN_WEB_PATH+"uploaddocumet/")
        doc =  Documento()
        doc.id_client = Cliente.objects.get(user_id = request.user.id)
        doc.file.save(arquivo.name, arquivo)
        doc.save()
        return redirect(GESTIN_WEB_PATH+"uploadeddocumets/")
        
        
@login_required
def documentosCarregados(request):
    cli = Cliente.objects.get(user_id = request.user.id)
    documents = Documento.objects.filter(id_client=cli.id)
    response =render(request,'uploadeddocs.html',{"user":request.user,
                                                  "documents":documents
                                                     })
    return response