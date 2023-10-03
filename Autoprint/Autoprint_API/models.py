from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Agente(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=500)
    token = models.CharField(max_length=512)
    foto = models.CharField()
    
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
    id_impressora = models.ForeignKey(Impressora, on_delete=models.CASCADE)
    #ID de confirmacao do lado do cliente e id de confirmacao do lado da maquina agente
    idConf_inpre = models.IntegerField()
    idConf_cli = models.IntegerField()
    data_pedido = models.DateField()
    data_conclusao =  models.DateField()

class Impressao(models.Model):
    id = models.AutoField(primary_key=True)
    id_client = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    documento = models.CharField()
    data_criacao = models.DateField()
    pedido = models.IntegerField()
    #faltam outros atributos
    