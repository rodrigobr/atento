# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from models import MobileCompany, Cellphone, Promotor, Rede, Loja, Marca, Ranking

class AdminMarca(ModelAdmin):
    list_display = ('name',)

class AdminMobileCompany(ModelAdmin):
    list_display = ('name',)

class AdminCellphone(ModelAdmin):
    list_display = ('marca', 'name',)

class AdminPromotor(ModelAdmin):
    list_display = ('name',)

class AdminRede(ModelAdmin):
    list_display = ('name',)

class AdminLoja(ModelAdmin):
    list_display = ('name', 'rede', 'codigo',)

class AdminRanking(ModelAdmin):
    list_display = ('loja', 'mobilecompany', 'cellphone', 'promotor', 'quantidade',)


admin.site.register(Marca, AdminMarca)
admin.site.register(MobileCompany, AdminMobileCompany)
admin.site.register(Cellphone, AdminCellphone)
admin.site.register(Promotor, AdminPromotor)
admin.site.register(Rede, AdminRede)
admin.site.register(Loja, AdminLoja)
admin.site.register(Ranking, AdminRanking)
