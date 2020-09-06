from django.conf import settings
from django.db import models


class Perfil(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, default=None, null=True, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=50, null=True)
    pontuacao = models.IntegerField(max_length=10, null=True)
    nivel = models.IntegerField(max_length=1, null=True)
    nome = models.CharField(max_length=100, null=True)


class Produtos(models.Model):
    user = models.ManyToManyField(Perfil)
    nome = models.CharField(max_length=20, null=True)


class Insignas(models.Model):
    titulo = models.CharField(max_length=50, null=True)
    descricao = models.CharField(max_length=250, null=True)


class Myinsignas(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    insigna = models.ForeignKey(Insignas, on_delete=models.CASCADE)


class Vendas(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    foto = models.CharField(max_length=30, null=True)
    titulo = models.CharField(max_length=20, null=True)
    descricao = models.TextField(max_length=250, null=True)
    preco = models.FloatField(null=True)