from django.urls import path,include
from django.contrib.auth import views as auth_views
import os
from .views import * 


app_name = 'Autoprint_API'

urlpatterns = [
    path('downloadfile/<str:ficheiro>/',downloadFiles,name="downloadfile"),
    path('verpdf/<str:pdfname>/',readpdf,name="verpdf"),
    #AGENTE
    path('pedidos/agentejson/',pedidosDoAgenteJson,name="pedidosdoagentejson"),   
]