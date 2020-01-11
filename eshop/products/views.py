from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import Template,Context
# Create your views here.


def add_product(request):
    return render(request,'add_product.html')


