from django.db import models

class Cliente(models.Model):
    """Clientes de advogados."""

    TIPO_CLIENTE = (
        ('PF','Pessoa Física'),
        ('PJ','Pessoa Jurídica'),
    )
    nome = models.CharField(max_length=512)
    tipo = models.CharField(max_length=2,choices=TIPO_CLIENTE,default='PF')
    documento = models.CharField(max_length=40)
    rg = models.CharField(max_length=25)
    email = models.EmailField(max_length=254, null=True,blank=True)
    nascimento = models.DateField(null=True,blank=True, auto_now=False, auto_now_add=False)

    class Meta:
        """Meta definition for Cliente."""

        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return nome

