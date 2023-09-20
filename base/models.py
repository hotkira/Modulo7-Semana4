from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    lido = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f'{self.nome}: [{self.email}]'
    class Meta:
        verbose_name = 'Formulário de Contato'
        verbose_name_plural = 'Formulários de Contatos'
        ordering = ['-data']


class Reserva(models.Model):
    nomeDoPet = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    dia = models.DateField()
    observacoes = models.TextField()
    data = models.DateTimeField(auto_now_add=True)