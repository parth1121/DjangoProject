from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from codefirstapp.models import Product
from codefirstapp import forms

def test(request):
    # Product.objects.create(product_name='Wheel Chair', product_desc='used for accessbvility patient')
    product_list1 =Product.objects.filter(id__gt =4)
    product_list2 = Product.objects.filter(id__lt=4)
    product_list3 = product_list1.union(product_list2)
    print(product_list3.query)

    form = forms.ProductForm()
    if request.method == 'POST':
        form = forms.ProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['productName'])
            print(form.cleaned_data['productDesc'])
    return render(request, 'index.html',{'form':form})
