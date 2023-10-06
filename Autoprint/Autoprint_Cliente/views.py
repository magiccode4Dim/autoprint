from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

USER_WEB_PATH = "user/"
GESTIN_WEB_PATH = "impressoes/"

USER_URLS = {
    "LOGIN":USER_WEB_PATH+"login",
    "LOGOUT":USER_WEB_PATH+"logout",
    "PROFILE":USER_WEB_PATH+"profile",
    "PASSWORD_CHANGE":USER_WEB_PATH+"password_change",
    "REGISTER":USER_WEB_PATH+"register",
    "PASSWORD_RESET":USER_WEB_PATH+"password_reset",
    "CONFIGS":USER_WEB_PATH+"configs",
}

GESTIM_URLS = {
    "UPLOAD_DOCUMENT":GESTIN_WEB_PATH+"uploaddocumet",
    "DOCUMENT_TO_PRINT":GESTIN_WEB_PATH+"uploaddocumet"
}



# Create your views here.
@login_required
def dashboardCliente(request):
    response =render(request,'clientdashboard.html',{"user":request.user,
                                                     "USER_URLS":USER_URLS,
                                                     "GESTIM_URLS":GESTIM_URLS
                                                     })
    return response
    