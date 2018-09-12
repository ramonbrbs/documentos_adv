from django.urls import path
from . import views

urlpatterns = [
    
    path('editar/<int:pk>', views.ClienteUpdate.as_view(), name='cliente_editar',),
    path('cadastro/', views.ClienteCreate.as_view(), name='cliente_cadastrar',),
    path('', views.ClienteList.as_view(), name='cliente_listar',),
    path('<int:pk>/', views.ClienteDetalhe.as_view(), name='cliente_detalhe',),
    #path('editar_sociedade/<int:pk>', views.SociedadeUpdate.as_view(), name='alterar_sociedade',),
]