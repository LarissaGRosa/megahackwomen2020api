from rest_framework import serializers

from apirules.models import Vendas, Perfil


class VendasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendas
        fields = '__all__'


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'