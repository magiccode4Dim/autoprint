from django.urls import path,include
from django.contrib.auth import views as auth_views
import os
from .views import * 


app_name = 'Autoprint_Agente'

urlpatterns = [
    path('pedidosdoagente/',pedidosDoAgente,name="pedidosdoagente"),
    path('viewpdfforprint/',viewpdfforprint,name="viewpdfforprint")    
]