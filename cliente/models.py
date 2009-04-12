from django.db import models
 
class Bairro(models.Model):
  bairro = models.CharField(max_length=150)
  def __unicode__(self):
    return self.bairro
  class Meta:
    db_table = 'bairro'
 
class Logradouro(models.Model):
  bairro = models.ForeignKey(Bairro)
  logradouro = models.CharField(max_length=250)
  def __unicode__(self):
    return self.logradouro
  class Meta:
    db_table = 'logradouro'
 
class GrupoVencimento(models.Model):
  grupo_vencimento = models.CharField("Grupo",max_length=20)
  dia_vencimento = models.IntegerField("Dia",max_length=2)
  def __unicode__(self):
    return self.grupo_vencimento
  class Meta:
    db_table = 'grupovencimento'
    verbose_name = 'Grupo de Vencimento'
    verbose_name_plural = 'Grupos de Vencimento'
    unique_together = ['grupo_vencimento']
 
class Cliente(models.Model):
  TIPO_PESSOA = (
    ('F','Pessoa Fisica'),
    ('J','Pessoa Juridica'),
    ('R','Representante de Pessoa Juridica')
  )
  grupovencimento = models.ForeignKey(GrupoVencimento,verbose_name="Grupo")
  nome = models.CharField("Nome/Razao Social",max_length=200)
  apelido = models.CharField("Apelido/Nome Fantasia",max_length=200,blank=True,null=True)
  cpf = models.CharField("CPF/CNPJ",max_length=14,unique=True)
  rg = models.CharField("RG/IE",max_length=11,blank=True,null=True)
  orgao_rg = models.CharField("Orgao RG",max_length=6,blank=True,null=True)
  tipo_pessoa = models.CharField(max_length=1,choices=TIPO_PESSOA)
  data_nascimento = models.DateField(blank=True,null=True)
  data_cadastro = models.DateField(auto_now_add=True)
  logradouro = models.ForeignKey(Logradouro,verbose_name='Endereco',blank=True,null=True)
  numero = models.CharField(max_length=50,blank=True,null=True)
  referencia = models.CharField(max_length=250,blank=True,null=True)
 
  cep = models.PositiveIntegerField(max_length=8,blank=True,null=True)
  def __unicode__(self):
    return self.nome
  class Meta:
    db_table = 'cliente'
    unique_together = ('nome','cpf','rg')