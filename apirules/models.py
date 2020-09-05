from django.conf import settings
from django.db import models


class Perfil(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, default=None, null=True, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=50, null=True)
    pontuacao = models.IntegerField(max_length=10, null=True)
    nivel = models.IntegerField(max_length=1, null=True)
    nome = models.CharField(max_length=100, null=True)
