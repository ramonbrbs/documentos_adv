from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    SEXO_ADVOGADO = (
        ('M','Masculino'),
        ('F','Feminino'),
    )
    oab_estado = models.CharField(max_length=2)
    oab = models.CharField(max_length=30, blank=True)
    nacionalidade = models.CharField(max_length=120)
    estado_civil = models.CharField(max_length=120)
    sociedade = models.CharField(max_length=256,null=True, blank=True)
    sociedade_cnpj = models.CharField(max_length=256,null=True, blank=True)
    sexo = models.CharField(max_length=2,choices=SEXO_ADVOGADO, null=True, blank=True)