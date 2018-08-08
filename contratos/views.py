from django.shortcuts import render,redirect
from clientes.models import Cliente
from django.template.loader import render_to_string
from weasyprint import HTML
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View
import tempfile
from xhtml2pdf import pisa
from io import BytesIO
import pdfkit
from .forms import GerarContratoForm
# Create your views here.


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

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
    html  = template.render({})
    

def procuracao(request):
    return render_to_pdf2('procuracao.html')

def gerarContratos(request):
    
    
    if request.method == 'POST':
        form = GerarContratoForm(request.POST, user=request.user)
        if form.is_valid():
            cli = form.cleaned_data['cliente']
            return render_to_pdf2('procuracao.html', {'cliente' : cli,'advogado':request.user})
            

        
    else:
        form = GerarContratoForm(user=request.user)
    return render(request,'gerar.html',{'form':form} )
