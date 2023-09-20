from django.shortcuts import render
from base.forms import ContatoForm
from base.forms import ReservaForm

# Create your views here.
def inicio(request):
  return render(request, 'inicio.html')


def contato(request):
  sucesso = False

  form = ContatoForm(request.POST or None)
  print(form.as_p())
  if (form.is_valid()):
    form.save()
    sucesso = True
  
  context = {
    'telefone': '81 99999999',
    'nome': 'Fabio Mariano',
    'formulario': form,
    'sucesso': sucesso
  }

  return render(request, 'contato.html', context)


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
  return render(request, 'reserva.html', context)
