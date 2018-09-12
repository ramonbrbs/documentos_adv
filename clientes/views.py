from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cliente
from django.shortcuts import redirect
from django.http import Http404
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Field, Div, Fieldset, Row, HTML, Submit, Hidden
from crispy_forms.bootstrap import InlineRadios

class ClienteCreate(CreateView):
    model = Cliente
    template_name = 'cliente_create.html'
    fields = ('nome','tipo','sexo','documento','rg','email','nascimento','nacionalidade','estado_civil','endereco','profissao','telefone','banco','banco_agencia','banco_operacao','banco_conta','mae','pai')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.show_form_errors = True
        form.helper.form_method = 'post'
        form.helper.form_action = 'cliente_cadastrar'

        form.helper.layout = Layout(
            Fieldset('Informações Pessoais',
            
            InlineRadios('tipo'),
            Field('nome',wrapper_class='form-group'),
            Field('profissao'),
            Field('nacionalidade'),
             Div(
                Div(Field('email',),css_class="col-md-6"),
                Div(Field('telefone',),css_class="col-md-3"),
                css_class="row",
            ),
            
            Div(
                Div(InlineRadios('sexo',),css_class="col-md-4"),
                Div(Field('nascimento',),css_class="col-md-4"),
                css_class="row",
            ),

            Div(
                Div(Field('pai',),css_class="col-md-6"),
                Div(Field('mae',),css_class="col-md-6"),
                css_class="row",
            ),
            
            Div(
                Div(Field('documento',),css_class="col-md-4"),
                Div(Field('rg',),css_class="col-md-4"),
                Div(Field('estado_civil',),css_class="col-md-4"),
                css_class="row",
            ),
            Field("endereco")
            ),
            HTML("<hr>"),
            Fieldset('Informações Bancárias',
                Field('banco'),
                Div(
                    Div(Field('banco_conta',),css_class="col-md-3"),
                    Div(Field('banco_agencia',),css_class="col-md-2"),
                    Div(Field('banco_operacao',),css_class="col-md-2"),
                    css_class='row'
                ),
                
            ),
            Submit("Enviar",'Enviar')
            
        )
        return form
    

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.advogado = self.request.user
        self.object.save()
        return redirect('/')

class ClienteDetalhe(DetailView):
    model = Cliente
    template_name = 'cliente_detail.html'

class ClienteList(ListView):
    model = Cliente
    template_name = 'cliente_list.html'

    def get_queryset(self):
        queryset = Cliente.objects.filter(advogado = self.request.user)
        print(queryset)
        return queryset


class ClienteUpdate(UpdateView):
    model = Cliente
    fields = '__all__'
    template_name = 'cliente_create.html'

    model = Cliente
    template_name = 'cliente_create.html'
    fields = ('nome','tipo','sexo','documento','rg','email','nascimento','nacionalidade','estado_civil','endereco','profissao','telefone','banco','banco_agencia','banco_operacao','banco_conta','mae','pai')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.show_form_errors = True
        form.helper.form_method = 'post'

        form.helper.layout = Layout(
            Fieldset('Informações Pessoais',
            
            InlineRadios('tipo'),
            Field('nome',wrapper_class='form-group'),
            Field('profissao'),
            Field('nacionalidade'),
             Div(
                Div(Field('email',),css_class="col-md-6"),
                Div(Field('telefone',),css_class="col-md-3"),
                css_class="row",
            ),
            
            Div(
                Div(InlineRadios('sexo',),css_class="col-md-4"),
                Div(Field('nascimento',),css_class="col-md-4"),
                css_class="row",
            ),

            Div(
                Div(Field('pai',),css_class="col-md-6"),
                Div(Field('mae',),css_class="col-md-6"),
                css_class="row",
            ),
            
            Div(
                Div(Field('documento',),css_class="col-md-4"),
                Div(Field('rg',),css_class="col-md-4"),
                Div(Field('estado_civil',),css_class="col-md-4"),
                css_class="row",
            ),
            Field("endereco")
            ),
            HTML("<hr>"),
            Fieldset('Informações Bancárias',
                Field('banco'),
                Div(
                    Div(Field('banco_conta',),css_class="col-md-3"),
                    Div(Field('banco_agencia',),css_class="col-md-2"),
                    Div(Field('banco_operacao',),css_class="col-md-2"),
                    css_class='row'
                ),
                
            ),
            Submit("Enviar",'Enviar')
            
        )
        return form
    
   
    def dispatch(self, request, *args, **kwargs):
        self.obj = self.get_object()
        if(self.obj.advogado != request.user):
            return redirect('/')
        else:
            return super().dispatch(request, *args, *kwargs)