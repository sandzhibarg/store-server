from django import forms

from orders.models import Orders

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('first_name', 'last_name', 'email', 'address')

