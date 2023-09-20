from django.shortcuts import render

from reserva.forms import ReservaForm

# Create your views here.
def reserva(request):
  sucesso = False

  form = ReservaForm(request.POST or None)

  if (form.is_valid()):
    form.save()
    sucesso = True
  
  context = {
    'formulario': form,
    'sucesso': sucesso
  }
  return render(request, 'reserva_de_banho.html', context)