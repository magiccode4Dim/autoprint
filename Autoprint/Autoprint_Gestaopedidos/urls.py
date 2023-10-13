from django.urls import path,include
from django.contrib.auth import views as auth_views
import os
from .views import * 
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Autoprint_Gestaopedidos'

urlpatterns = [
    path('uploaddocumet/',carregarDocumentos.as_view(),name="uploaddocumente"), 
    path('uploadeddocumets/',documentosCarregados,name="uploadeddocumentes"),
    path('adicionarimpressao/<str:documento>',adicionarImpressao.as_view(),name="adicionarimpressao"),    
    #path('minhasimpressoes/',impressoesCriadas,name="minhasimpressoes"),   
    #path('criarpedidoimpressao/',criarPedidoImpressao.as_view(),name="criarpedidoimpressao"), 
    path('pedidoscriados/',pedidosCriados,name="pedidoscriados"),
    path('confirmarpedido/',confirmarPedido.as_view(),name="confirmarpedido"), 
]

#configurando o proprio django como servidor de arquivos de media estatico somente para ambiente de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)