from django.db import models
from advogados.models import Usuario

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
    sexo = models.CharField(max_length=2,choices=SEXO_CLIENTE)
    documento = models.CharField(max_length=40)
    rg = models.CharField(max_length=25)
    email = models.EmailField(max_length=254, null=True,blank=True)
    nascimento = models.DateField(null=True,blank=True, auto_now=False, auto_now_add=False)
    advogado = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nacionalidade = models.CharField(null=True,blank=True, max_length=120)
    estado_civil = models.CharField(null=True,blank=True, max_length=70)
    endereco = models.CharField(null=True,blank=True, max_length=250)
    profissao = models.CharField(blank=True,null=True, max_length=150)

    class Meta:
        """Meta definition for Cliente."""

        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome

