from django import forms
from django.forms import ModelForm
from .models import Item, Warehouse


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'warehouse':forms.Select(attrs={'class':'form-control'})
        }
        
class WarehouseForm(ModelForm):
    class Meta:
        model = Warehouse
        fields = "__all__"
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'})
        }