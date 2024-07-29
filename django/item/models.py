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