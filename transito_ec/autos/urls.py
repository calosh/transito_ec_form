from django.conf.urls import patterns, url

from autos import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'vehiculos$', views.listado_vehiculos, name='listado_vehiculos'),
    url(r'buscador$', views.buscador_placas, name='buscador_placas'),
    url(r'buscador_2$', views.buscador_placas_dos, name='buscador_placas_dos'),
    url(r'funcion_ajax/$', views.funcion_ajax, name='funcion_ajax'),
    url(r'funcion_ajax_dos/$', views.funcion_ajax_dos, name='funcion_ajax_dos'),
    # usando forms
    url(r'vehiculos_tipo/$', views.listado_vehiculos_tipo, name='listado_vehiculos_tipo'),
    url(r'vehiculos_tipo2/$', views.listado_combustibles_provincia, name='listado_combustibles_provincia'),
    # url(r'provincia/(?P<id>\d+)$', views.provincia, name='provincia'),
    # url(r'provincia/(?P<id>\d+)/mivista/aplicacion$', views.provincia, name='provincia'),
)
