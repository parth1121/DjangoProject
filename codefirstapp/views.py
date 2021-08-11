from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from codefirstapp.models import Product
from codefirstapp import forms

def test(request):
    # Product.objects.create(product_name='Wheel Chair', product_desc='used for accessbvility patient')
    # product_list =Product.objects.all()
    form = forms.ProductForm()
    if request.method == 'POST':
        form = forms.ProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['productName'])
            print(form.cleaned_data['productDesc'])
    return render(request, 'index.html',{'form':form})
