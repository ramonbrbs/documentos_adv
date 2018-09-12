from django.db import models
from advogados.models import Usuario
from django.shortcuts import redirect, reverse

class Cliente(models.Model):
    """Clientes de advogados."""

    TIPO_CLIENTE = (
        ('PF','Pessoa Física'),
        ('PJ','Pessoa Jurídica'),
    )
    SEXO_CLIENTE = (
        ('M','Masculino'),
        ('F','Feminino'),
    )
    nome = models.CharField(max_length=512)
    tipo = models.CharField(max_length=2,choices=TIPO_CLIENTE,default='PF')
    sexo = models.CharField(max_length=2,choices=SEXO_CLIENTE, default='M')
    documento = models.CharField(max_length=40)
    rg = models.CharField(max_length=25)
    email = models.EmailField(max_length=254, null=True,blank=True)
    nascimento = models.DateField(null=True,blank=True, auto_now=False, auto_now_add=False)
    advogado = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nacionalidade = models.CharField(null=True,blank=True, max_length=120)
    estado_civil = models.CharField(null=True,blank=True, max_length=70)
    endereco = models.CharField(null=True,blank=True, max_length=250)
    profissao = models.CharField(blank=True,null=True, max_length=150)
    telefone = models.CharField(max_length=22)
    banco = models.CharField(max_length=256)
    banco_agencia = models.CharField(max_length=20,verbose_name="Agência")
    banco_operacao = models.CharField(max_length=120, verbose_name="Operação")
    banco_conta = models.CharField(max_length=70, verbose_name="Conta")
    mae = models.CharField(max_length=256, verbose_name="Nome da Mãe")
    pai = models.CharField(max_length=256, verbose_name="Nome do Pai")

    def get_absolute_url(self):
            return reverse('cliente_detalhe', args=[str(self.id)])
    class Meta:
        """Meta definition for Cliente."""

        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        permissions = (
            ('view_cliente','Ver Cliente'),
        )

    def __str__(self):
        return self.nome

