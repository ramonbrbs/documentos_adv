from django.contrib import admin
from .models import Contrato
from .forms import GerarContratoForm
from advogados.models import Usuario


@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    #usuario = Usuario.objects.get(pk=1)
    #form = GerarContratoForm(user=usuario)


    actions = ['set_genre_action']

    def set_genre_action(self, request, queryset):
        form = GerarContratoForm()

        return render(request, 'gerar.html',
            {'title': u'Choose genre',
             'objects': queryset,
             'form': form})
'''
    def get_form(self, request, obj=None, **kwargs):
        form = super(Contrato, self).get_form(request, obj, **kwargs)
        usuario = request.user
        return form

    '''


