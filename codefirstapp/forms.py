from django import forms
from django.core import validators

def startswithp(value):
    if value[0].lower() != 'p':
        raise forms.ValidationError('Name should be starts with p')

class ProductForm(forms.Form):
    productName = forms.CharField(widget = forms.PasswordInput)
    productDesc = forms.CharField(widget = forms.Textarea,validators = [startswithp, validators.MinLengthValidator(5)])

    def clean(self):
        print("validating form")
        form_data = super().clean()
        product_name = form_data['productName']
        print(product_name)