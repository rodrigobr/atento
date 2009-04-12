from atento.cliente.models import *
from django.forms import *
 
class ClienteForm(ModelForm):
  nome = CharField(max_length=200)
  cpf = CharField(max_length=140)
  class Meta:
    model = Cliente