from django import forms
from clientes.models import Cliente


class GerarContratoForm(forms.Form):
    tipos_acoes = (
        ('Ação de Benefício Previdenciáriovel', 'Ação de Benefício Previdenciário'),
        ('Defesa Criminal', 'Defesa Criminal'),
        ('Reclamatória Trabalhista','Reclamatória Trabalhista'),
        ('Ação de Família','Ação de Família'),
        ('Processo Tributário','Processo Tributário'),
    )
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.none())
    tipo_acao = forms.ChoiceField(choices=tipos_acoes)


    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(GerarContratoForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].queryset=queryset=Cliente.objects.filter(advogado=self.user)
    