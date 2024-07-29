# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Rifa, NumeroVendido

# @receiver(post_save, sender=Rifa)
# def criar_numeros_vendidos(sender, instance, created, **kwargs):
#     print(f"Objeto: {instance}")
#     print(f"Criado: {created}")

#     if created:
#         print('Criando números vendidos')
#         print("Quantia de números: ", instance.quantidade_numeros)
#         for numero in range(1, instance.quantidade_numeros + 1):
#             numero_vendido, created = NumeroVendido.objects.get_or_create(
#                 numero=numero, 
#                 rifa_relacionada=instance
#             )
#             instance.numeros.add(numero_vendido)
            
#         print("Numeros criados: ", instance.numeros.all())
#         print("Item rifado: ", instance.items.all())
#         instance.quantidade_numeros = instance.numeros.all().count()
#         print("Quantidade de números vendidos: ", instance.quantidade_numeros_vendidos)
#         instance.get_valor_total()
#         instance.get_valor_numero()
#         instance.save() 