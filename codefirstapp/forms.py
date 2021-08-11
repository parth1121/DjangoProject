from django import forms

class ProductForm(forms.Form):
    productName = forms.CharField()
    productDesc = forms.CharField()