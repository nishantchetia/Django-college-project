from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Homepage.as_view(), name='Homepage'),
    url(r'^contact$', views.Contactpage.as_view(), name='contact_us'),
    url(r'^hydraulic$', views.Hydraulic.as_view(), name='Hydraulic'),
    url(r'^igo$', views.igo.as_view(), name='igo'),
    url(r'^mcw$', views.mwo.as_view(), name='mcw'),
    url(r'^rco$', views.rco.as_view(), name='rco'),
    url(r'^spo$', views.spo.as_view(), name='spo'),
    url(r'^tfo$', views.TFO.as_view(), name='tfo'),
    url(r'^tur$', views.tur.as_view(), name='tur'),
    url(r'^wro$', views.wro.as_view(), name='wro'),
    url(r'^ING$', views.ING.as_view(), name='ing'),
    url(r'^ao$', views.ao.as_view(), name='ao'),
    url(r'^AGO$', views.AGO.as_view(), name='ago'),
    url(r'^rdc$', views.rdc.as_view(), name='rdc'),
]
