from django import forms
from .models import Rifa
from item.models import Item

class RifaAdminForm(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(
        queryset=Item.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    quantidade_numeros = forms.IntegerField(min_value=1, required=True)

    class Meta:
        model = Rifa
        fields = '__all__'
