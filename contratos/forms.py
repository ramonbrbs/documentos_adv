from django import forms
from clientes.models import Cliente
from advogados.models import Sociedade
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

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
    sociedade = forms.ModelChoiceField(queryset=Sociedade.objects.none())
    cidade = forms.CharField(max_length=512, required=True)
    
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    helper.form_method = 'POST'

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(GerarContratoForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].queryset=queryset=Cliente.objects.filter(advogado=self.user)
        self.fields['sociedade'].queryset=queryset=Sociedade.objects.filter(advogado=self.user)

class ContratoHonorariosForm(forms.Form):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.none())

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(ContratoHonorariosForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].queryset=queryset=Cliente.objects.filter(advogado=self.user)
    