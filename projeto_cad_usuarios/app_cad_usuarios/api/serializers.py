from rest_framework import serializers
from app_cad_usuarios import models


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = '__all__'


class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pagamento
        fields = '__all__'        