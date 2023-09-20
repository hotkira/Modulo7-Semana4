from django.contrib import admin
from django.contrib import messages

from base.models import Contato

@admin.action(description='Marcar Registro(s) como lido(s)')
def marcar_como_lido(modeladmin, request, queryset):
  queryset.update(lido=True)
  modeladmin.message_user(request, 'Registro atualizado para lido!!', messages.SUCCESS)


# Register your models here.
@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
  list_display = ['nome', 'email', 'mensagem', 'data', 'lido']
  search_fields = ['nome', 'email']
  list_filter = ['data', 'lido']
  actions = [marcar_como_lido]
