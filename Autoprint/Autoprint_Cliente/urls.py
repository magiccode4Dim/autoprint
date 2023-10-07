from django.urls import path,include
from django.contrib.auth import views as auth_views
import os
from .views import * 


app_name = 'Autoprint_Cliente'

urlpatterns = [
    path('dashboard/',dashboardCliente,name="dashboardcliente"),    
]