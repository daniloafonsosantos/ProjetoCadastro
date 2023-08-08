
from django.contrib import admin
from django.urls import path, include
from app_cad_usuarios import views
from app_cad_usuarios.api import viewsets as clienteviewsets

from rest_framework import routers

from django.conf.urls.static import static
from django.conf import settings

route = routers.DefaultRouter()
route.register('api/clientes', clienteviewsets.ClienteViewSet ,basename="Clientes")




urlpatterns = [
    path('api/pagamentos/', clienteviewsets.PagamentoView.as_view()),    
    # path('admin/', admin.site.urls),
    # path('', views.home,name='home'),
    path('', views.home,name='home'),    
    path('clientes/', views.gradeclientes,name='listagem_gradeclientes'),          
    path('pagamentosauto/', views.pagamentoautomatico,name='pagamentoautomatico'),                 
    
    # path('', views.gradeclientes,name='home'), 

    # ####################### AQUIIIII API GET FUNCIONANDO
       


    path('usuarios/', views.usuarios,name='listagem_usuarios'),    
    path('cliente/', views.cadastroclientes,name='cadastro_clientes'),       

    path('clientesgrade/', views.clientes,name='listagem_clientes'),        
    
    path('pagamentoscad/', views.cadastropagamentos,name='cadastro_pagamentos'),             
    path('pagamentos/', views.pagamentos,name='listagem_pagamentos'),         
  
    

    
    path('pagamentosgrade/', views.gradepagamentos,name='listagem_gradepagamentos'),      
    
    path('',include(route.urls)) ,      
    
    
    
     
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
