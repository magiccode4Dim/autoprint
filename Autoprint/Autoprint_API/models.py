from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Agente(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=500, default="")
    token = models.CharField(max_length=512, default="")
    foto = models.CharField(default="")
    
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=50)
    foto = models.CharField()
    
class Impressora(models.Model):
    id = models.AutoField(primary_key=True)
    id_agent = models.ForeignKey(Agente, on_delete=models.CASCADE)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=200)
    localizacao = models.CharField(max_length=800)
    foto = models.CharField()
    
class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    id_client = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_agent = models.ForeignKey(Agente, on_delete=models.CASCADE)
    #ID de confirmacao do lado do cliente e id de confirmacao do lado da maquina agente
    idConf_inpre = models.IntegerField()
    idConf_cli = models.IntegerField()
    data_pedido = models.DateField(default=timezone.now)
    data_conclusao =  models.DateField(null=True, default=None)
    isconfirmed = models.BooleanField(default=False)

class Documento(models.Model):
    id = models.AutoField(primary_key=True)
    id_client = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    file = models.FileField(upload_to='DOCUMENTOS/')


class Impressao(models.Model):
    id = models.AutoField(primary_key=True)
    id_client = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_document = models.ForeignKey(Documento, on_delete=models.SET_NULL, null=True) #permitir que o documento seja apagado sem que a impressa
                                                                                    #sem apagar a impressao tambem
    data_criacao = models.DateField(default=timezone.now)
    pedido = models.IntegerField(default=-1)
    #faltam outros atributos
    

    
