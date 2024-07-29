from django.shortcuts import render
from .models import Rifa, NumeroVendido
from config.models import Conta
import base64
from io import BytesIO
from PIL import Image

def index(request):
    return render(request, "rifa/index.html")

def rifa(request, rifa_id):
    rifa = Rifa.objects.get(id=rifa_id)
    rifa.save()
    print(rifa.numeros.all())
    numeros = NumeroVendido.objects.filter(rifa_relacionada=rifa)
    print(numeros)
    return render(request, "rifa/rifa.html", {"rifa": rifa, "Numeros": numeros})

def detalhes_numero(request, rifa_id, numero_id):
    rifa = Rifa.objects.get(id=rifa_id)

    numero = NumeroVendido.objects.get(id=numero_id, rifa_relacionada=rifa)
    print(numero)
    print(rifa)
    return render(request, 'rifa/numero_detail.html', {'numero': numero, 'rifa': rifa})

def comprar_numero(request, rifa_id, numero_id):
    rifa = Rifa.objects.get(id=rifa_id)

    numero = NumeroVendido.objects.get(id=numero_id, rifa_relacionada=rifa)
    print(numero)
    print(rifa)

    print("TAMO NO COMPRAR NUMERO")

    conta = Conta.objects.get(nome='Rifas')

    return render(request, 'rifa/pagamento.html', {'numero': numero, 'rifa': rifa, 'qr_code': conta.gerar_pix(str(rifa.valor_numero))})