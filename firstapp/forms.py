from django import forms
from firstapp.models import Order, Pizza

class OrderForm(forms.ModelForm):
    pizza = forms.ModelChoiceField(queryset=Pizza.objects.all(), widget=forms.HiddenInput)
    # Displays only 3 fields from model Order
    class Meta:
        model = Order
        fields = ('pizza', 'name', 'phone')