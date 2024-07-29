from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("rifa/<int:rifa_id>/", views.rifa, name="rifa"),
    path("rifa/<int:rifa_id>/detalhes/<int:numero_id>", views.detalhes_numero, name="numero_detail"),
    path("rifa/<int:rifa_id>/comprar/<int:numero_id>", views.comprar_numero, name="comprar_numero"),
]