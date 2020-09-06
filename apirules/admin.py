from django.contrib import admin

# Register your models here.
from apirules.models import Perfil, Vendas

admin.site.register(Perfil)
admin.site.register(Vendas)