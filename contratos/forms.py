from django import forms
from clientes.models import Cliente


class GerarContratoForm(forms.Form):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.none())
    tipo = forms.ChoiceField(choices=((1,'Procuração'),))


    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(GerarContratoForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].queryset=queryset=Cliente.objects.filter(advogado=self.user)