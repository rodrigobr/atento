from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^atento/', include('atento.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    (r'^media/(.*)','django.views.static.serve',{'document_root':'/home/rodrigo/project/atento/media/'}),
    #(r'contact/', 'atento.contato.views.main'),
    (r'^cliente/list/$','atento.cliente.views.list'),
    (r'^cliente/add/$','atento.cliente.views.add'),
    (r'^cliente/delete/$','atento.cliente.views.delete'),
    (r'^cliente/edit/$','atento.cliente.views.edit'),
    (r'^cliente/update/$','atento.cliente.views.update'),
    (r'^cliente/search/$','atento.cliente.views.search'),
    (r'^auth/login/$','django.contrib.auth.views.login', {'template_name': '/home/rodrigo/project/atento/templates/loginform.html'}),
    (r'^auth/logout/$','django.contrib.auth.views.logout_then_login'),
    (r'^cliente/getlogradouros/$','atento.cliente.views.getlogradouros'),
    (r'^grappelli/', include('grappelli.urls')),

)
