from django.urls import path

from rest_framework.routers import SimpleRouter

from rest_api.views import *
from . import views

app_name = 'rest_api'

routers = SimpleRouter()
routers.register('agendamento', AgendamentoModelViewSet)

routers.register('reserva_banho', ReservaModelViewSet, basename='reserva_banho')

routers.register('petshop', PetshopModelViewSet)

routers.register('contato-mvs', ContatoModelViewSet)

routers.register('categoria-animal', CategoriaAnimalModelViewSet, basename='categoria-animal')
routers.register('reservas-por-categoria', ReservasPorCategoriaViewSet, basename='reservas-por-categoria')


urlpatterns = [
  path('hello_world', hello_world, name='hello_world'),
  path('contato/listar', listarTodosContatos, name='listar_contatos'),
  path('contato/<int:id>', obterUm, name='obter_contato_pelo_id' ),
  path('contato/<str:nome>', obterPeloNome, name="obter_contato_pelo_nome"),
  path('contato/novo', criarContato, name='criar_contato'),
  path('contato/deletar/<int:id>', deletarContato, name='deletar_contato')
]

urlpatterns += routers.urls
