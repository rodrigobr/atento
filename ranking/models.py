# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Marca(models.Model):
    class Meta:
        ordering = ('name',)
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class Cellphone(models.Model):
    class Meta:
        ordering = ('name','marca')
    name = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca)
    status = models.BooleanField(default=True)
    def __unicode__(self):
        return self.name

class MobileCompany(models.Model):
    name = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    def __unicode__(self):
        return self.name

class Promotor(models.Model):
    name = models.CharField(max_length=120)
    class Meta:
        ordering = ('name',)
    def __unicode__(self):
        return self.name
        
class Rede(models.Model):
    name = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ('name',)    

class Loja(models.Model):
    rede = models.ForeignKey(Rede)
    name = models.CharField(max_length=50)
    codigo = models.IntegerField()
    endereco = models.CharField(max_length=120)
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = ('Loja')

class Ranking(models.Model):
    loja = models.ForeignKey(Loja)
    marca = models.ForeignKey(Marca)
    cellphone = models.ForeignKey(Cellphone)
    promotor = models.ForeignKey(Promotor)
    mobilecompany = models.ForeignKey(MobileCompany)
    quantidade = models.IntegerField()


    class Meta:
        ordering = ('loja', 'promotor')
    
