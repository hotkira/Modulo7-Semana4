from django.db import models

# Create your models here.
class Reserva(models.Model):
  OPCOES_DE_TURNO = (
    ('manha', 'Manhã'),
    ('tarde', 'Tarde')
  )
  OPCOES_DE_TAMANHO = (
    (0, 'Pequeno'),
    (1, 'Médio'),
    (2, 'Grande')
  )
  nomeDoPet = models.CharField(max_length=50, verbose_name='Nome do PET')
  telefone = models.CharField(max_length=15, verbose_name='Telefone')
  observacoes = models.TextField(blank=True, verbose_name='Observações')
  data = models.DateField(verbose_name='Data')
  turno = models.CharField(max_length=5, choices=OPCOES_DE_TURNO, verbose_name='Turno')
  tamanho = models.IntegerField(choices=OPCOES_DE_TAMANHO, verbose_name='Tamanho')
  petshop = models.ForeignKey(
    'Petshop',
    verbose_name='petshops',
    related_name='reservas',
    on_delete=models.CASCADE,
    blank=True,
    null=True
  )
  categoria_animal = models.ForeignKey(
    'CategoriaAnimal',
    verbose_name='Categoria do Animal',
    on_delete=models.CASCADE,
    related_name='reservas',
    blank=True,
)

  def __str__(self):
    return f'{self.nomeDoPet} - {self.data} - {self.turno}'
  
  class Meta:
    verbose_name = 'Reserva de Banho'
    verbose_name_plural = 'Reservas de Banho'
    ordering = ['-data']


class Petshop(models.Model):
  nome = models.CharField(verbose_name="Nome do petshop", max_length=50)
  endereco = models.CharField(verbose_name="Endereço", max_length=150)
  numero = models.CharField(verbose_name="Número", max_length=10)
  bairro = models.CharField(verbose_name="Bairro", max_length=30)
  
class CategoriaAnimal(models.Model):
    nome_categoria = models.CharField(max_length=50, verbose_name='Nome da Categoria')

    def __str__(self):
        return self.nome_categoria
