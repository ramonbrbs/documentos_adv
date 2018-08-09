from django.urls import path
from contratos import views

urlpatterns = [
    path('procuracao/', views.gerarProcuracao, name='contratos_procuracao',)
]