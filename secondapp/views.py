from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def secondtest(request):
    s = '<h1>First request of django app!!</h1>'
    return HttpResponse(s)
