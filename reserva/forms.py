from django import forms
from datetime import date

from reserva.models import Reserva

class ReservaForm(forms.ModelForm):

  def clean_data(self):
    data = self.cleaned_data['data']
    hoje = date.today()

    if data < hoje:
      raise forms.ValidationError('Não é possível reservar um banho para uma data no passado')

    quantidadeDeReservasParaODiaEscolhido = Reserva.objects.filter(data=data).count()

    if quantidadeDeReservasParaODiaEscolhido >= 4:
      raise forms.ValidationError('O limite máximo de reservas para este dia já foi alcançado')

    return data

  class Meta:
    fields = ['nomeDoPet', 'telefone', 'data', 'turno', 'tamanho', 'observacoes']
    model = Reserva
    widgets = {
      'data': forms.DateInput(attrs={ 'type': 'date'})
    }