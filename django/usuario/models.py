from django.db import models

class InformacoesUsuario(models.Model):

    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    cotas_compradas = models.ManyToManyField('rifa.Rifa', related_name='cotas_compradas', blank=True)
    rifas_ganhas = models.ManyToManyField('rifa.Rifa', related_name='rifas_ganhas', blank=True)

    tradelink = models.URLField(blank=True, null=True)

    itens_ganhos = models.ManyToManyField('item.ItemRifado', related_name='itens', blank=True)

    def __str__(self):
        return self.user.username
    
    def get_rifas_em_andamento(self):
        return self.cotas_compradas.filter(ativa=True)
    
    def get_rifas_finalizadas(self):
        return self.cotas_compradas.filter(ativa=False)
    
    def get_rifas_ganhas(self):
        return self.rifas_ganhas.all()
    
    def get_itens_ganhos(self):
        return self.itens_ganhos.all()
    
    def get_itens_ganhos_disponiveis_para_saque(self):
        return self.itens_ganhos.filter(retirado=False)
    
    def get_itens_ganhos_retirados(self):
        return self.itens_ganhos.filter(retirado=True)