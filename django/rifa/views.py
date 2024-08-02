from django.shortcuts import render, redirect, get_object_or_404
from .models import Rifa, NumeroVendido
from config.models import Conta
import base64
from io import BytesIO
from PIL import Image

def index(request):
    return render(request, "rifa/index.html")

def rifa(request, rifa_id, refresh=None):
    rifa = get_object_or_404(Rifa, id=rifa_id)
    rifa = Rifa.objects.get(id=rifa_id)
    rifa.save()
    numeros = NumeroVendido.objects.filter(rifa_relacionada=rifa)
    
    if refresh is None:
        refresh = 0

    return render(request, "rifa/rifa.html", {"rifa": rifa, "Numeros": numeros, 'refresh': refresh})

def detalhes_numero(request, numero_id):

    numero = NumeroVendido.objects.get(id=numero_id)

    return render(request, 'rifa/numero_detail.html', {'numero': numero, 'rifa': numero.rifa_relacionada})

def comprar_numero(request, rifa_id, numero_id):
    rifa = Rifa.objects.get(id=rifa_id)

    numero = NumeroVendido.objects.get(id=numero_id, rifa_relacionada=rifa)

    conta = Conta.objects.get(nome='Rifas')

    return render(request, 'rifa/pagamento.html', {'numero': numero, 'rifa': rifa, 'qr_code': conta.gerar_pix(str(rifa.valor_numero))})

def reservar_numero(request, numero_id):

    numero = NumeroVendido.objects.get(id=numero_id)

    numero.status = 'R'
    numero.save()

    return redirect('rifa', rifa_id=numero.rifa_relacionada.id, refresh=1)