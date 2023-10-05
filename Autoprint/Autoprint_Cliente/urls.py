from django.urls import path,include
from django.contrib.auth import views as auth_views
import os
from .views import * 

urlpatterns = [
    path('dashboard/',dashboardCliente,name="dashboardcliente"),    
]