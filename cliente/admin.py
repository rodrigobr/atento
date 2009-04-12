from django.contrib import admin
from atento.cliente.models import *
 
class ClienteAdmin(admin.ModelAdmin):  
  date_hierarchy = 'data_cadastro'
  ordering = ['nome']
  list_filter = ('id','nome')
  search_fields = ('nome','cpf')
 
admin.site.register(Cliente,ClienteAdmin)
 
class GrupoVencimentoAdmin(admin.ModelAdmin): pass
admin.site.register(GrupoVencimento,GrupoVencimentoAdmin)
 
class BairroAdmin(admin.ModelAdmin): pass
admin.site.register(Bairro,BairroAdmin)
 
class LogradouroAdmin(admin.ModelAdmin): pass
admin.site.register(Logradouro,LogradouroAdmin)