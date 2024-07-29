from django.shortcuts import render
from .models import Rifa, NumeroVendido
def index(request):
    return render(request, "rifa/index.html")

def rifa(request, rifa_id):
    rifa = Rifa.objects.get(id=rifa_id)
    rifa.save()
    print(rifa.numeros.all())
    numeros = NumeroVendido.objects.filter(rifa_relacionada=rifa)
    print(numeros)
    return render(request, "rifa/rifa.html", {"rifa": rifa, "Numeros": numeros})