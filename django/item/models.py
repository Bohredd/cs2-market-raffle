from django.db import models

class Item(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    imagem = models.ImageField(upload_to='item', null=True, blank=True)
    mercado_relacionado = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    

class ItemRifado(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    retirado = models.BooleanField(default=False)
    data_retirada = models.DateTimeField(null=True, blank=True)
    rifa_relacionada = models.ForeignKey('rifa.Rifa', on_delete=models.CASCADE)
    numero_relacionado = models.ForeignKey('rifa.NumeroVendido', on_delete=models.CASCADE, null=True, blank=True)
