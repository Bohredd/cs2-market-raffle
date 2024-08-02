from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    re_path(r'^rifa/(?P<rifa_id>\d+)/(?P<refresh>\d+)?$', views.rifa, name='rifa'),
    path("rifa/detalhes/<int:numero_id>", views.detalhes_numero, name="numero_detail"),
    path("rifa/<int:rifa_id>/comprar/<int:numero_id>", views.comprar_numero, name="comprar_numero"),
    path('rifa/reservar/<int:numero_id>', views.reservar_numero, name='reservar_numero'),
]