from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin


class Usuario(AbstractUser):
    SEXO_ADVOGADO = (
        ('M','Masculino'),
        ('F','Feminino'),
    )
    oab_estado = models.CharField(max_length=2)
    oab = models.CharField(max_length=30, blank=True)
    nacionalidade = models.CharField(max_length=120)
    estado_civil = models.CharField(max_length=120)
    sociedade_nome = models.CharField(max_length=256,null=True, blank=True)
    sociedade_cnpj = models.CharField(max_length=256,null=True, blank=True)
    sexo = models.CharField(max_length=2,choices=SEXO_ADVOGADO, null=True, blank=True)

    def has_perm(self, perm, obj=None):
        if obj is not None:
            print("aaaaaaaaaaaa")
        if hasattr(obj,"advogado"):
            if obj.advogado.id == self.id:
                return True
            else:
                return False
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

class Sociedade(models.Model):
    nome = models.CharField(max_length=256)
    cnpj = models.CharField(max_length=20)
    endereco = models.CharField(max_length=256)
    advogado = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    oab = models.CharField(max_length=256)
    conta = models.CharField(max_length=256,null=True, blank=True)
    agencia = models.CharField(max_length=256,null=True, blank=True)
    banco = models.CharField(max_length=256,null=True, blank=True)

