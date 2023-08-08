from django.shortcuts import render
from .models import Usuario, Cliente, Pagamento

# Create your views here.
# def home(request):
#     return render(request, 'usuarios/home.html')
def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')    
    novo_usuario.idade = request.POST.get('idade')  
    novo_usuario.save()  

    
    usuarios = {
        'usuarios' : Usuario.objects.all()    
    }
    return render(request,'usuarios/usuarios.html',usuarios)         


def clientes(request):
    
    
    print(request)
    baixaauto = request.POST.get('baixaauto')

    # if baixaauto:
    print('danilo')
    novo_cliente = Cliente()
    
    
    print(request)
    print('danilo')    
    print(request.FILES)
    
    if request.method == 'POST' and request.FILES.get('imagem1'):
        # imagem = request.FILES.get('imagem1')
        
        # print(imagem)
        # # Faça o que deseja com a imagem aqui, por exemplo, salvar no disco:
        # with open('C:\\ProjetoCadastro\\projeto_cad_usuarios\\media\\testeee.jpeg', 'wb') as destino:
        #     for chunk in imagem.chunks():
        #         destino.write(chunk)    
    
    
        novo_cliente.imagemcliente = request.FILES.get('imagem1')
    
    novo_cliente.nome = request.POST.get('nome')
    novo_cliente.data_nascimento = request.POST.get('data_nascimento')       
    novo_cliente.dataemprestimo = request.POST.get('dataemprestimo')

    novo_cliente.valoremprestado = request.POST.get('valoremprestado')
    novo_cliente.valorjurosmensal = request.POST.get('valorjurosmensal')
    novo_cliente.valorquitado = request.POST.get('valorquitado')
        
    if novo_cliente.valoremprestado == novo_cliente.valorquitado:
        novo_cliente.quitado100 = True

    # novo_cliente.sobrenome = request.POST.get('sobrenome')
    # novo_cliente.data_nascimento = request.POST.get('data_nascimento')   
    # novo_cliente.email = request.POST.get('email')
    novo_cliente.save()
    # else:
    #     print('bora q bora')    

    clientes = {
        'clientes' : Cliente.objects.all()    
    }
    return render(request,'clientes/clientes.html',clientes)                 
    # return render(request,'usuarios/usuarios.html',usuarios)     

def gradeclientes(request):
    print('LISTA CLIENTES')
    clientes = {
        'clientes' : Cliente.objects.all()    
    }
    return render(request,'clientes/clientes.html',clientes)                 

def cadastroclientes(request):
    return render(request,'clientes/cadastrocliente.html')   


def pagamentos(request):
    print('Daniloooo')
    print('gravou pagamento')

    novo_pagamento = Pagamento()    
    # novo_pagamento.id_cliente = Cliente(pk=request.POST.get('id_cliente'))
    novo_pagamento.id_cliente = Cliente(pk=request.POST.get('id_cliente'))    
    
    print(novo_pagamento.id_cliente)
    novo_pagamento.datapagamento = request.POST.get('datapagamento')    
    print(novo_pagamento.datapagamento)
    novo_pagamento.valorpago = request.POST.get('valorpago')  
    novo_pagamento.valorquitado = request.POST.get('valorquitado')
    novo_pagamento.save()  

    
    pagamentos = {
        'pagamentos' : Pagamento.objects.all()    

    }
    return render(request,'pagamentos/pagamentos.html',pagamentos)    
    
def cadastropagamentos(request):
    print('oiiiie')
    if request.method == 'POST':
        print('entrou')
        id = request.POST.get('hiddeid')
        print('Danilo' + str(id))
    else:
        id = None

    

    context = {'id': id}
    return render(request,'pagamentos/cadastropagamentos.html',context)     


def gradepagamentos(request):
    pagamentos = {
        'pagamentos' : Pagamento.objects.all()    

    }
    return render(request,'pagamentos/pagamentos.html',pagamentos)     

def pagamentoautomatico(request):
    pagamentos = {
        'pagamentos' : Pagamento.objects.all()    

    }
    return render(request,'pagamentos/pagamentoautomatico.html',pagamentos)    
