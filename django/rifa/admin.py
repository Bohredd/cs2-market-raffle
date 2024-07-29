from django.contrib import admin
from .models import Rifa, NumeroVendido
from .forms import RifaAdminForm

class RifaAdmin(admin.ModelAdmin):
    form = RifaAdminForm
    list_display = ['id', 'valor_rifa', 'quantidade_numeros', 'quantidade_numeros_vendidos']
    actions = ['realizar_sorteio']

    def realizar_sorteio(self, request, queryset):
        for rifa in queryset:
            resultado = rifa.realizar_sorteio(request)
            self.message_user(request, resultado)
    realizar_sorteio.short_description = "Realizar sorteio da rifa selecionada"

    def save_model(self, request, obj, form, change):
        if not change:
            items = form.cleaned_data.get('items')
            quantidade_numeros = form.cleaned_data.get('quantidade_numeros')
            obj.criando_rifa(items, quantidade_numeros)
            obj.save()
        else:
            super().save_model(request, obj, form, change)

admin.site.register(Rifa, RifaAdmin)
admin.site.register(NumeroVendido)
