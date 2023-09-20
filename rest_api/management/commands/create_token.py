from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    help = 'Criar um token para um usuário'

    def add_arguments(self, parser: CommandParser) -> None:
      parser.add_argument('--username', required=True)
      parser.add_argument('--password', required=True)

    def handle(self, *args, **options):
      username = options['username']
      password = options['password']

      self.stdout.write(
        self.style.WARNING(f'Criando o usuário {username}')
      )

      user = User(username=username)
      user.first_name = username
      user.set_password(password)
      user.save()

      self.stdout.write(
        self.style.WARNING('Usuário criado com sucesso!')
      )

      token = Token.objects.create(user=user)
      
      self.stdout.write(
        self.style.WARNING(f'Token criado: {token}')
      )

