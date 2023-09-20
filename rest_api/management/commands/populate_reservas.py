from django.core.management.base import BaseCommand

from model_bakery import baker


from reserva.models import Reserva

class Command(BaseCommand):
  help = 'Criar os dados fakes do model Reserva'

  def handle(self, *args, **options):
    quantidadeDeReservas = 100

    self.stdout.write(
      self.style.WARNING(f'Executando comando para criar {quantidadeDeReservas} reservas fakes')
    )

    for i in range(quantidadeDeReservas):
      reserva = baker.make(Reserva)
      reserva.save()
      self.stdout.write(
        self.style.WARNING(f'Criada a reserva numero {i}')
      )

    self.stdout.write(
      self.style.SUCCESS('Criou todas as reservas!!')
    )