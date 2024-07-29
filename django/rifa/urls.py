from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("rifa/<int:rifa_id>/", views.rifa, name="rifa"),
]