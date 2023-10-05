from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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


# Create your views here.
@login_required
def dashboardCliente(request):
    response =render(request,'clientdashboard.html',{"user":request.user, "USER_URLS":USER_URLS})
    return response
    