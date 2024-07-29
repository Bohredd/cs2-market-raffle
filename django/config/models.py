from django.db import models
from rifa.pix import GerarPix

class Conta(models.Model):
    nome = models.CharField(max_length=255)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    chave = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    
    def get_saldo(self):
        return self.saldo
    
    def gerar_pix(self, valor):
        return GerarPix(
            nome=self.nome,
            chavepix=self.chave,
            valor=valor,
            cidade='',
        ).gerarPayload()
    
    def creditar(self, valor):
        self.saldo += valor
        self.save()

    def debitar(self, valor):
        self.saldo -= valor
        self.save()