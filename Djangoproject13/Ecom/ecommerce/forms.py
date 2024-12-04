# ecommerce/forms.py
from django import forms
from .models import Product  # Assuming you have a Product model

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']
