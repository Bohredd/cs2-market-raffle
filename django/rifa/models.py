from django.db import models
import random
from django.utils import timezone
from config.models import Conta

class NumeroVendido(models.Model):
    numero = models.IntegerField()
    comprador = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    data_aquisicao = models.DateTimeField(blank=True, null=True)
    rifa_relacionada = models.ForeignKey('Rifa', on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(
        max_length=1,
        choices=[
            ('D', 'Disponível'),
            ('V', 'Vendido'),
            ('R', 'Reservado'),
        ],
        default='D'
    )

    def __str__(self):
        return f'{self.numero} - {self.comprador} - {self.data_aquisicao} - {self.rifa_relacionada}'
    
    def validar_pagamento(self):
        if self.status == 'R':
            self.status = 'V'
            self.data_aquisicao = timezone.now()
            self.save()
            Conta.objects.get(nome='Rifas').saldo += self.rifa_relacionada.valor_numero

    def reservar_numero(self, comprador):
        if self.status == 'D':
            self.status = 'R'
            self.comprador = comprador
            self.save()

class VencedorItem(models.Model):
    item = models.ForeignKey('item.Item', on_delete=models.CASCADE)
    numero = models.ForeignKey(NumeroVendido, on_delete=models.CASCADE)
    rifa = models.ForeignKey('Rifa', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.item} - {self.numero}'

class Rifa(models.Model):
    items = models.ManyToManyField('item.Item', related_name='rifas')
    valor_rifa = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantidade_numeros = models.IntegerField(null=True, blank=True, default=0)
    numeros = models.ManyToManyField(NumeroVendido, related_name='numeros', null=True, blank=True)
    quantidade_numeros_vendidos = models.IntegerField(null=True, blank=True, default=0)
    valor_numero = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    data_inicio = models.DateTimeField(auto_now_add=True)
    ativa = models.BooleanField(default=True)
    numeros_ganhadores = models.ManyToManyField(NumeroVendido, related_name='ganhadores', blank=True)
    arrumado = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
    
    def get_valor_total(self):
        self.valor_rifa = sum(self.items.all().values_list('valor', flat=True))

    def get_valor_numero(self):
        if self.quantidade_numeros > 0:
            self.valor_numero = self.valor_rifa / self.quantidade_numeros

    def get_porcentagem_progresso(self):
        if self.quantidade_numeros > 0:
            return (self.quantidade_numeros_vendidos / self.quantidade_numeros) * 100
        return 0
    
    def get_valor_arrecadado(self):
        if self.valor_numero is not None and self.quantidade_numeros_vendidos is not None:
            return self.valor_numero * self.quantidade_numeros_vendidos
        return 0
    
    def sortear_ganhadores(self, request):
        if self.quantidade_numeros_vendidos == self.quantidade_numeros or request.user.is_staff:
            ganhadores = {}

            for item in self.items.all():
                numero_vencedor = None
                print(request.user.is_staff)

                if request.user.is_staff:
                    numeros = NumeroVendido.objects.filter(rifa_relacionada=self)
                    print(f"Numeros: {numeros}")
                else:
                    numeros = NumeroVendido.objects.filter(data_aquisicao__isnull=False)

                if not numeros.exists():
                    print(f"Não há números vendidos disponíveis para o item {item}")
                    continue

                while not numero_vencedor:
                    random_number = random.randint(1, self.quantidade_numeros)
                    print(f"Número aleatório gerado: {random_number}")
                    numero_vencedor = numeros.filter(numero=random_number).first()

                    if not numero_vencedor:
                        print(f"Número {random_number} não encontrado entre os números vendidos.")

                print(f"Número vencedor para o item {item}: {numero_vencedor}")

                ganhadores[item] = numero_vencedor
                VencedorItem.objects.create(item=item, numero=numero_vencedor, rifa=self)
                self.numeros_ganhadores.add(numero_vencedor)

            return ganhadores

        return None

    
    def realizar_sorteio(self, request):
        ganhadores = self.sortear_ganhadores(request)
        if ganhadores:
            resultados = [f'O número vencedor para o item {item} é {vencedor.numero}, comprado por {vencedor.comprador}.' for item, vencedor in ganhadores.items()]
            return '\n'.join(resultados)
        return 'Nenhum número vendido.'

    def get_quantia_numeros_vendidos(self):
        return self.numeros.filter(data_aquisicao__isnull=False).count()

    def save(self, *args, **kwargs):
        if self.pk:
            self.get_valor_total()
            self.get_valor_numero()
            self.quantidade_numeros_vendidos = self.get_quantia_numeros_vendidos()
        super().save(*args, **kwargs)
    
    def get_numeros_vendidos(self):
        return self.numeros.filter(data_aquisicao__isnull=False).values_list('numero', flat=True)
    
    def get_numeros_disponiveis(self):
        numeros_vendidos = self.get_numeros_vendidos()
        return [numero for numero in range(1, self.quantidade_numeros + 1) if numero not in numeros_vendidos]
    
    def transferir_item_rifado(self, item):
        pass
    
    def criando_rifa(self, items, quantidade_numeros):
        self.quantidade_numeros = quantidade_numeros
        self.save()
        
        for item in items:
            self.items.add(item)

        for numero in range(1, quantidade_numeros + 1):
            numero_vendido, created = NumeroVendido.objects.get_or_create(
                numero=numero, 
                rifa_relacionada=self
            )
            self.numeros.add(numero_vendido)
        
        self.save()