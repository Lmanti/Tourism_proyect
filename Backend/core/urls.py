from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^hosting/$', views.CrudHosting),
    url(r'^hosting/([0-9]+)$', views.CrudHosting),
    url(r'^municipality/$', views.CrudMunicipality),
    url(r'^municipality/([0-9]+)$', views.CrudMunicipality),
    url(r'^ofert/$', views.CrudOfert),
    url(r'^ofert/([0-9]+)$', views.CrudOfert),
    url(r'^user/$', views.CrudUser),
    url(r'^user/([0-9]+)$', views.CrudUser),
    url(r'^turism/$', views.CrudTourist),
    url(r'^turism/([0-9]+)$', views.CrudTourist),
    url(r'^activitys/$', views.CrudActivity),
    url(r'^activitys/([0-9]+)$', views.CrudActivity),
    url(r'^restaurant/$', views.CrudRestaurant),
    url(r'^restaurant/([0-9]+)$', views.CrudRestaurant),
    url(r'^discovery/$', views.CrudDiscovery),
    url(r'^discovery/([0-9]+)$', views.CrudDiscovery),
    url(r'^reservation/$', views.CrudReservation),
    url(r'^reservation/([0-9]+)$', views.CrudReservation)
]