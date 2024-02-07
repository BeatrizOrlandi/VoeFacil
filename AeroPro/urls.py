from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('pilotos/', PilotoListView.as_view(), name='piloto_list'),
    path('comissarios/', ComissarioListView.as_view(), name='comissario_list'),
    path('passagens/comprar/<int:voo_id>/', PassagemCreateView.as_view(), name='passagem_create'),
    path('passagens/', PassagemListView.as_view(), name='passagem_list'),
    path('passagens/<int:passagem_id>/', PassagemDetailView.as_view(), name='passagem_detail'),
    path('pilotos/cadastrar/', PilotoCreateView.as_view(), name='piloto_create'),
    path('comissarios/cadastrar/', ComissarioCreateView.as_view(), name='comissario_create'),
    path('aeronaves/cadastrar/', AeronaveCreateView.as_view(), name='aeronave_create'),
    path('passageiros/cadastrar/', PassageiroCreateView.as_view(), name='passageiro_create'),
    path('companhias_aereas/cadastrar/', CompanhiaAereaCreateView.as_view(), name='companhia_aerea_create'),
    path('funcionarios/cadastrar/', FuncionarioCreateView.as_view(), name='funcionario_create'),
    path('comissarios/', ComissarioListView.as_view(), name='comissario_list'),
    path('aeronaves/', AeronaveListView.as_view(), name='aeronave_list'),
    path('passageiros/', PassageiroListView.as_view(), name='passageiro_list'),
    path('companhias_aereas/', CompanhiaAereaListView.as_view(), name='companhia_aerea_list'),
    path('funcionarios/', FuncionarioListView.as_view(), name='funcionario_list'),
    path('voo/cadastrar/', VooCreateView.as_view(), name='voo_create')
]