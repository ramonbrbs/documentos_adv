from django.urls import path
from contratos import views

urlpatterns = [
    path('procuracao/', views.gerarProcuracao, name='contratos_procuracao',),
    path('honorarios/', views.gerarHonorarios, name='contratos_honorarios',),
    path('',views.index, name='contratos_index'),
]