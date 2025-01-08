from django.shortcuts import render
from .models import *


def home_page(request):
    return render(request, 'home.html')

def product_list(request):
    data = Product.objects.all()
    return render(request, 'product_list.html', {'data':data})

def product_detail(request, product_id):
    data = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'data':data})