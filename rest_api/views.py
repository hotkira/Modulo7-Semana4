from django.shortcuts import render
import django_filters
from rest_framework import generics
from rest_framework import viewsets
from django_filters import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  (
   IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny, IsAdminUser
)

from base.models import Contato
from reserva.models import Reserva, Petshop, CategoriaAnimal
from rest_api.serializers import (
  AgendamentoModelSerializer, ContatoModelSerializer, PetshopSerializer, ReservaModelSerializer, CategoriaAnimalSerializer
)

class PetshopModelViewSet(ReadOnlyModelViewSet):
  queryset = Petshop.objects.all()
  serializer_class = PetshopSerializer
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticatedOrReadOnly]


class AgendamentoModelViewSet(ModelViewSet):
  queryset = Reserva.objects.all()
  serializer_class = AgendamentoModelSerializer
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticatedOrReadOnly]

  

class CategoriaAnimalModelViewSet(ModelViewSet):
  queryset = CategoriaAnimal.objects.all()
  serializer_class = CategoriaAnimalSerializer
    

class ReservaFilterSet(django_filters.FilterSet):
    class Meta:
        model = Reserva
        fields = {
            'categoria_animal__nome_categoria': ['icontains'],
            'nomeDoPet': ['icontains']
        }

class ReservaModelViewSet(ModelViewSet):
    serializer_class = ReservaModelSerializer
    queryset = Reserva.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReservaFilterSet  # Use a classe de filtro aqui

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAdminUser()]
      
class ReservasPorCategoriaViewSet(viewsets.ModelViewSet):
  serializer_class = ReservaModelSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_class = ReservaFilterSet
  ordering_fields = '__all__'

  def get_queryset(self):
      categoria_id = self.kwargs.get('categoria_id')
      if categoria_id:
          return Reserva.objects.filter(categoria_animal=categoria_id)
      return Reserva.objects.all()
  
#assim funciona o filtro
# class ReservaModelViewSet(ModelViewSet):
#   serializer_class = ReservaModelSerializer
#   queryset = Reserva.objects.all()
#   filter_backends = [DjangoFilterBackend]
#   filterset_fields = {
#       'nomeDoPet': ['icontains']
#     } 
  
#   def get_permissions(self):
#     #VERIFICA SE O METODO É SEGURO
#     if self.action=='create':
#       return [AllowAny()]  
#     return [IsAdminUser()]
  


class ContatoModelViewSet(ModelViewSet):
  queryset = Contato.objects.all()
  serializer_class = ContatoModelSerializer
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticated]



# Create your views here.
@api_view(['GET', 'POST'])
def hello_world(request):
  if request.method == 'POST':
    nome = request.data.get('nome')
    mensagemCustomizada = f'Olá, {nome}'
    return Response({ 'mensagem': mensagemCustomizada })

  return Response({ 'mensagem': 'Hello World'})

@api_view(['GET'])
def listarTodosContatos(request):
  contatos = Contato.objects.all()
  dados = []

  for contato in contatos:
    dados.append({
      "nome": contato.nome,
      "email": contato.email,
      "mensagem": contato.mensagem,
      "id": contato.id
    })

  return Response({ "contatos": dados })


@api_view(['GET'])
def obterUm(request, id):
  contato = Contato.objects.filter(id=id)

  if len(contato) == 0:
    return Response({ "error": "Contato inexistente"})

  dado = {
    "nome": contato[0].nome,
    "email": contato[0].email,
    "mensagem": contato[0].mensagem
  }

  return Response({ "contato": dado})


@api_view(['POST'])
def criarContato(request):
  nome = request.data.get('nome')
  email = request.data.get('email')
  mensagem = request.data.get('mensagem')

  if nome == None or email == None or mensagem == None:
    return Response({ "error": "Preencha os campos obrigatórios: nome, email, mensagem"})

  novoContato = Contato.objects.create(nome=nome, email=email, mensagem=mensagem)
  dado = {
    "nome": novoContato.nome,
    "email": novoContato.email,
    "mensagem": novoContato.mensagem,
    "id": novoContato.id
  }

  return Response({'contato': dado})


@api_view(['DELETE'])
def deletarContato(request, id):
  contato = Contato.objects.filter(id=id)

  if len(contato) == 0:
    return Response({ "error": "Contato inexistente!"})
  
  contato[0].delete()

  return Response({ "mensagem": "Contato deletado!" })

@api_view(['GET'])
def obterPeloNome(request, nome):
  contato = Contato.objects.filter(nome=nome)

  if len(contato) == 0:
    return Response({ "error": "Contato inexistente"})

  dado = {
    "nome": contato[0].nome,
    "email": contato[0].email,
    "mensagem": contato[0].mensagem
  }
  return Response({ "contato": dado})
