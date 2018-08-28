from django.shortcuts import render,redirect
from clientes.models import Cliente
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View
import tempfile
from io import BytesIO
import pdfkit
from .forms import GerarContratoForm, ContratoHonorariosForm
# Create your views here.



def render_to_pdf2(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pdfkit.from_string(html, False)
    #pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    
    return HttpResponse(pdf, content_type='application/pdf')
    #return None
    

def proc2(request):
    template = get_template('2.html')
    html  = template.renderp({})
    

def procuracao(request):
    return render_to_pdf2('procuracao.html')

def gerarProcuracao(request):
    if request.method == 'POST':
        form = GerarContratoForm(request.POST, user=request.user)
        if form.is_valid():
            cli = form.cleaned_data['cliente']
            acao = form.cleaned_data['tipo_acao']
            print(acao)
            return render_to_pdf2('procuracao.html', {'cliente' : cli,'advogado':request.user,'acao':acao})       
    else:
        form = GerarContratoForm(user=request.user)
    return render(request,'gerar.html',{'form':form})


def gerarHonorarios(request):
    if request.method == 'POST':
        form = ContratoHonorariosForm(request.POST, user=request.user)
        if form.is_valid():
            cli = form.cleaned_data['cliente']
            return render_to_pdf2('honorarios.html', {'cliente' : cli,'advogado':request.user})       
    else:
        form = ContratoHonorariosForm(user=request.user)
    return render(request,'gerar.html',{'form':form})
