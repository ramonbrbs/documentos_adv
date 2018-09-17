from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Usuario, Sociedade
from django.http import Http404
from django.shortcuts import redirect, reverse
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Field, Div, Fieldset, Row, HTML, Submit, Hidden
from crispy_forms.bootstrap import InlineRadios
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class SociedadeUpdate(LoginRequiredMixin,UpdateView):
    model = Sociedade
    template_name = 'cadastro_sociedade.html'
    fields = ('nome', 'cnpj', 'endereco', 'oab', 'banco', 'conta', 'agencia')

    def dispatch(self, request, *args, **kwargs):
        self.obj = self.get_object()
        if self.obj.advogado != request.user:
            return redirect('/')
        else:
            return super().dispatch(request, *args, *kwargs)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.show_form_errors = True

        form.helper.layout = Layout(
            Fieldset('Informações Gerais',
                        Div(
                            Div(Field('nome',), css_class="col-md-6"),
                            Div(Field('cnpj',), css_class="col-md-3"),
                            Div(Field('oab',), css_class="col-md-3"),
                            css_class="row",
                        ),
                        Field('endereco'),
                        
                     ),
            HTML("<hr>"),
            Fieldset('Informações Bancárias',
                Div(
                    Div(Field("banco"), css_class="col-md-4"),
                    Div(Field("agencia"), css_class="col-md-4"),
                    Div(Field("conta"), css_class="col-md-4"),
                    css_class="row"
                )
            ),
            Submit("Enviar",'Enviar',css_class="btn btn-success")
        )
        return form

class SocieadeDetail(LoginRequiredMixin,DetailView):
    model = Sociedade
    template_name = 'detalhe_sociedade.html'

    def dispatch(self, request, *args, **kwargs):
        self.obj = self.get_object()
        if self.obj.advogado != request.user:
            return redirect('/')
        else:
            return super().dispatch(request, *args, *kwargs)


class SociedadeList(LoginRequiredMixin,ListView):
    model = Sociedade
    template_name = 'lista_sociedade.html'

    def get_queryset(self):
        queryset = Sociedade.objects.filter(advogado=self.request.user)
        print(queryset)
        return queryset


class SociedadeCreate(LoginRequiredMixin,CreateView):
    model = Sociedade
    fields = ('nome', 'cnpj', 'endereco', 'oab', 'banco', 'conta', 'agencia')
    template_name = 'cadastro_sociedade.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.show_form_errors = True

        form.helper.layout = Layout(
            Fieldset('Informações Gerais',
                        Div(
                            Div(Field('nome',), css_class="col-md-6"),
                            Div(Field('cnpj',), css_class="col-md-3"),
                            Div(Field('oab',), css_class="col-md-3"),
                            css_class="row",
                        ),
                        Field('endereco'),
                        
                     ),
            HTML("<hr>"),
            Fieldset('Informações Bancárias',
                Div(
                    Div(Field("banco"), css_class="col-md-4"),
                    Div(Field("agencia"), css_class="col-md-4"),
                    Div(Field("conta"), css_class="col-md-4"),
                    css_class="row"
                )
            ),
            Submit("Enviar",'Enviar',css_class="btn btn-success")
        )
        return form

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.advogado = self.request.user
        self.object.save()
        return redirect('/')


class AdvogadoCreate(CreateView):
    helper = FormHelper()
    model = Usuario
    fields = ('first_name', 'last_name', 'sexo', 'email', 'password',
              'oab_estado', 'oab', 'nacionalidade', 'estado_civil')
    template_name = 'cadastro_usuario.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.layout = Layout(
            Fieldset('Informações Pessoais','first_name', 'last_name', 'sexo', 'email', 'password',
              'oab_estado', 'oab', 'nacionalidade', 'estado_civil'),
              
        )
        
        return form

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # things
        self.object.username = self.object.email
        self.object.set_password(self.object.password)
        self.object.save()

        return redirect('/')

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect('/')
        else:
            return super().dispatch(request, *args, *kwargs)


class AdvogadoUpdate(LoginRequiredMixin,UpdateView):
    model = Usuario
    fields = ('first_name', 'last_name', 'sexo', 'email', 'password',
              'oab_estado', 'oab', 'nacionalidade', 'estado_civil')
    template_name = 'cadastro_usuario.html'

    def dispatch(self, request, *args, **kwargs):
        self.obj = self.get_object()
        if(self.obj.id != request.user.id):
            return redirect('/')
        else:
            return super().dispatch(request, *args, *kwargs)


'''
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        if(self.object.id != request.user.id):
            raise Http404 
        return super(AdvogadoUpdate, self).get(request, *args, **kwargs)
'''
