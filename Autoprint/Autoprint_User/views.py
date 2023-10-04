from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
# Create your views here.
WEB_PATH = '/user'

CATEGORIAS = ["Estudante", "Funcionario","Outro"]

#redirect to login
def redirect_login(request):
    return redirect(WEB_PATH+'/login')

#Logout
@login_required
def logOut(request):
    logout(request)
    return render(request,'logout.html')

#cadastrar utilizadores
class register(View):
    def get(self, request, *args, **kwargs):
        error_message = request.GET.get('error')
        return render(request,'register.html',{"error":error_message,"cats":CATEGORIAS})
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        # Verificar se as senhas coincidem
        if request.POST['password'] != confirm_password:
            return redirect(WEB_PATH+"/register/?error=Passwords does not equals")
            #self.get(self, request)
        # Verificar se o nome de usuário já existe
        if User.objects.filter(username=username).exists():
            return redirect(WEB_PATH+"/register/?error=Username Existes")
            #self.get(self, request)
        # Criar o novo usuário automaticamente
        User.objects.create_user(
            username=username, 
            password=password, 
            first_name=first_name,
            last_name=last_name,
            email=email)
        # Redirecionar para uma página de sucesso ou fazer login automaticamente
        return render(request,'register_done.html',{'user':request.user})


#Trocar Senha
#O dispatch é o metodo responsavel pelo rooteamento entao o login_required sera aplicado a ele
@method_decorator(login_required, name='dispatch')
class change_password(View):
    def get(self, request, *args, **kwargs):
        error_message = request.GET.get('error')
        return render(request,'change_password.html',{"error":error_message})
    def post(self, request, *args, **kwargs):
        old_password = request.POST['old_password']
        user = request.user
        #se as passwords nao forem iguais
        if(not check_password(old_password,user.password)):
            #deve retornar para o get
            return  redirect(WEB_PATH+"/password_change/?error=Password not mach, try again")   
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']
        if(new_password1!=new_password2):
            return redirect(WEB_PATH+"/password_change/?error=Passwords does not equals")
        user.set_password(new_password1)
        user.save()
        return render(request,'change_password_done.html',{'user':request.user})
