
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
from django.views import View
from rest_framework import viewsets

from codefirstapp.models import Product
from codefirstapp import forms
from codefirstapp.serializer import ProductSerializer


def test(request):
    print("in between pre ad post processing")
    print(10/0)
    # Product.objects.create(product_name='Wheel Chair', product_desc='used for accessbvility patient')
    product_list1 =Product.objects.filter(id__gt =4)
    product_list2 = Product.objects.filter(id__lt=4)
    product_list3 = product_list1.union(product_list2)
    print(product_list3.query)
    # request.session.set_test_cookie()
    form = forms.ProductForm()
    cnt = request.session.get('cnt', 0)
    newcnt = cnt +1
    request.session['cnt'] = newcnt
    print( newcnt)
    request.session.set_expiry(10)
    print(request.session.get_expiry_date())
    print(request.session.get_expiry_age())
    if request.method == 'POST':
        form = forms.ProductForm(request.POST)
        if form.is_valid():
            if 'count' in request.COOKIES:
                newcount = int(request.COOKIES['count']) + 1
            else:
                newcount = 1
            response = render(request, 'index.html',{'form':form})
            response.set_cookie('count', newcount)
            print(newcount)
            print(form.cleaned_data['productName'])
            print(form.cleaned_data['productDesc'])
            return response
    else:
        return render(request, 'index.html', {'form': form})

def testCookie(request):
    if request.session.test_cookie_worked():
        print("cookie worked success")
        return HttpResponse("worked Successfully")
    return HttpResponse("not worked")


class ProductList(View):
    def get(self, request):
        list = Product.objects.all()
        count = Product.objects.count()
        item_list =[]
        for item in list:
            item_list.append({
            'product_name':item.product_name,
            'product_desc' : item.product_desc
            })

        data = {
            'itemlist': item_list,
            'itemcount': count
        }
        return JsonResponse(data)


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
