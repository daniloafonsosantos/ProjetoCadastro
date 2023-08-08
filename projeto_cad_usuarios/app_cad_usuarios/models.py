from django.conf import settings
from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()

def upload_image(instance, filename):
    return f"{instance.nome}-{filename}"

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    nomefiador = models.CharField(max_length=100,null=True)
    sobrenome = models.CharField(max_length=100,default='2022-01-01')
    data_nascimento = models.DateField()
    email = models.CharField(max_length=100, default='email')
    dataemprestimo = models.DateField(default='2022-01-01')
    chavepix = models.CharField(max_length=100,null=True)
    valoremprestado = models.DecimalField(max_digits = 6, decimal_places = 2,null=True)
    valorjurosmensal = models.DecimalField(max_digits = 6, decimal_places = 2,null=True)
    valorquitado = models.DecimalField(max_digits = 6, decimal_places = 2,null=True)
    quitado100 = models.BooleanField(default=False)
    imagemcliente = models.ImageField(upload_to=upload_image, blank=True, null=True) 
    imagemclientebase64 = models.TextField(max_length=400, default='SEM IMAGEM')


class Pagamento(models.Model):
    id_cliente = models.ForeignKey(Cliente,null=False,on_delete=models.PROTECT)        
    datapagamento = models.DateField()
    valorpago = models.DecimalField(max_digits = 6, decimal_places = 2,null=True)    
    valorquitado = models.DecimalField(max_digits = 6, decimal_places = 2,null=True)
    quitado100 = models.BooleanField(default=False)


    

class Telefone(models.Model):
    TIPOS_TELEFONE = (('celular','Celular'),('residencial','Residencial'),('comercial','Comercial'))
    tipo_telefone = models.CharField(max_length = 20, choices=TIPOS_TELEFONE)
    numero_telefone = models.CharField(max_length=20)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='telefones')
    

class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=20)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2) 

# class Cliente(models.Model):
#     nome = models.CharField(max_length=100)
#     sobrenome = models.CharField(max_length=100)
#     data_nascimento = models.DateField()
#     email = models.CharField(max_length=100)

# class Telefone(models.Model):
#     TIPOS_TELEFONE = (
#         ('celular', 'Celular'),
#         ('residencial', 'Residencial'),
#         ('comercial', 'Comercial'),
#     )
#     tipo_telefone = models.CharField(max_length=20, choices=TIPOS_TELEFONE)
#     numero_telefone = models.CharField(max_length=20)
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='telefones')

# class Endereco(models.Model):
#     rua = models.CharField(max_length=100)
#     numero = models.CharField(max_length=20)
#     bairro = models.CharField(max_length=100)
#     cidade = models.CharField(max_length=100)
#     estado = models.CharField(max_length=2)
#     cep = models.CharField(max_length=8)
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='enderecos')