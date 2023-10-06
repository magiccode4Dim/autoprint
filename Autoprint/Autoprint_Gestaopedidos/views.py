from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Autoprint_API.models import Documento, Cliente
import os

USER_WEB_PATH = "user/"

USER_URLS = {
    "LOGIN":USER_WEB_PATH+"login",
    "LOGOUT":USER_WEB_PATH+"logout",
    "PROFILE":USER_WEB_PATH+"profile",
    "PASSWORD_CHANGE":USER_WEB_PATH+"password_change",
    "REGISTER":USER_WEB_PATH+"register",
    "PASSWORD_RESET":USER_WEB_PATH+"password_reset",
    "CONFIGS":USER_WEB_PATH+"configs",
}

GESTIN_WEB_PATH = "impressoes/"

GESTIM_URLS = {
    "UPLOAD_DOCUMENT":GESTIN_WEB_PATH+"uploaddocumet",
    "DOCUMENT_TO_PRINT":GESTIN_WEB_PATH+"uploaddocumet"
}

#Verifica se o arquivo é permitido
def is_valid_file_type(file):
    file_extension = os.path.splitext(file.name)[1].lower()
    valid_extensions = ['.pdf', '.docx']
    return file_extension in valid_extensions


@method_decorator(login_required, name='dispatch')
class carregarDocumentos(View):
    def get(self, request, *args, **kwargs):
        response =render(request,'uploadfile.html',{"user":request.user, 
                                                "USER_URLS":USER_URLS,
                                                "GESTIM_URLS":GESTIM_URLS
                                                })
        return response
    def post(self, request, *args, **kwargs):
        arquivo = request.FILES['file']
        if not is_valid_file_type(arquivo):
            #se o arquivo nao for valido
            return HttpResponse("Arquivo invalido")
        doc =  Documento()
        doc.id_client = Cliente.objects.get(user_id = request.user.id)
        doc.file.save(arquivo.name, arquivo)
        doc.save()
        return HttpResponse("salvo com sucesso")
        