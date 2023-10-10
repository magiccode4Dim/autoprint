from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

USER_WEB_PATH = "user/"
GESTIN_WEB_PATH = "impressoes/"


# Create your views here.
@login_required
def dashboardCliente(request):
    response =render(request,'clientdashboard.html',{"user":request.user
                                                     })
    return response
    
    
