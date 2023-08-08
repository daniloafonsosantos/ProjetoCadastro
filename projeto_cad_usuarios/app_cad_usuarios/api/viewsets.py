from rest_framework import viewsets
from app_cad_usuarios.api import serializers
from app_cad_usuarios import models
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import date

class ClienteViewSet(viewsets.ModelViewSet):    
    serializer_class = serializers.ClienteSerializer
    queryset = models.Cliente.objects.all()
    
class PagamentoView(APIView):
   
    def post(self, request):
        print('request') 
        print(request)
        print(request.data)        
        serializer = serializers.PagamentoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)    