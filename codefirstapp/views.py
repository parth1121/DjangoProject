from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from codefirstapp.models import Product


def test(request):
    # Product.objects.create(product_name='Wheel Chair', product_desc='used for accessbvility patient')
    product_list =Product.objects.all()
    return render(request, 'index.html',{'product_list':product_list})
