
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField, PrimaryKeyRelatedField

from reserva.models import Reserva, Petshop, CategoriaAnimal
from base.models import Contato


class PetshopModelSerializer(ModelSerializer):
  reservas = HyperlinkedRelatedField(
    many=True,
    read_only=True,
    view_name='api:reserva'
  )

  class Meta:
    model = Petshop
    fields = '__all__'


# class PetshopNestedModelSerializer(ModelSerializer):
#   class Meta:
    model = Petshop
    fields = '__all__'


class PetshopRelatedFieldCustomSerializer(PrimaryKeyRelatedField):
  def __init__(self, **kwargs):
    self.serializer = PetshopModelSerializer
    super().__init__(**kwargs)

  def use_pk_only_optimization(self):
    return False
  
  def to_representation(self, value):
    return self.serializer(value, context=self.context).data


# class AgendamentoModelSerializer(ModelSerializer):
#   petshop = PetshopRelatedFieldCustomSerializer(
#     queryset=Petshop.objects.all(),
#     read_only=False
#   )

class AgendamentoModelSerializer(ModelSerializer):
  pethop = PetshopModelSerializer(read_only=True)

  class Meta:
    model = Reserva
    fields = '__all__'
    
class ReservaModelSerializer(ModelSerializer):
  categoria_animal = serializers.PrimaryKeyRelatedField(
     queryset=CategoriaAnimal.objects.all(),
     required=True,
     allow_null=False
  )
  class Meta:
    model = Reserva
    fields = '__all__'


class ContatoModelSerializer(ModelSerializer):
  class Meta:
    model = Contato
    fields = '__all__'
    
class PetshopSerializer(serializers.ModelSerializer):
  
  reservas = ReservaModelSerializer(many=True)
  
  class Meta:
    model = Petshop
    fields = [
      'id',
      'endereco',
      'numero',
      'bairro',
      'reservas',
              
    ]
    
class CategoriaAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaAnimal
        fields = '__all__'