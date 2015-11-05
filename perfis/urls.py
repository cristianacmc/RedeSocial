from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
     url(r'^$', views.index, name='index'),
     url(r'^perfis/(?P<perfil_id>\d+)$', views.exibir, name='exibir'),
     url(r'^perfis/(?P<perfil_id>\d+)/convidar$', views.exibir, name='exibir')
)
