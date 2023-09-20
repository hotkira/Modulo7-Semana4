from django.contrib import admin

from reserva.models import Reserva

# Register your models here.
@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
  list_display = ['nomeDoPet', 'telefone', 'data', 'turno', 'tamanho', 'observacoes']
  search_fields = ['nomeDoPet']
  list_filter = ['data', 'turno', 'tamanho']