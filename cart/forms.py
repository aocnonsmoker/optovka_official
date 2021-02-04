from django import forms
from .models import Orders

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(label='Количество')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)




class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['name', 'telephone', 'address', 'city', 'activity']