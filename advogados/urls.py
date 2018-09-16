from django.urls import path
from . import views

urlpatterns = [
    
    path('editar/<int:pk>', views.AdvogadoUpdate.as_view(), name='editar_advogado',),
    path('cadastro/', views.AdvogadoCreate.as_view(), name='cadastrar_advogado',),
    
    path('cadastro_sociedade/', views.SociedadeCreate.as_view(), name='cadastrar_sociedade',),
    path('lista_sociedade/', views.SociedadeList.as_view(), name='listar_sociedade',),
    path('sociedade/<int:pk>', views.SocieadeDetail.as_view(), name='detalhe_sociedade',),
    path('editar_sociedade/<int:pk>', views.SociedadeUpdate.as_view(), name='editar_sociedade',),
]