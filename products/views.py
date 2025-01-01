from django.shortcuts import render
from .models import *


def home_page(request):
    return render(request, 'products/home.html')

def product_page(request):
    query = request.GET.get('query', '')
    if query:
        data = Product.objects.filter(name__icontains=query)
    else:
        data = Product.objects.all()
    return render(request, 'products/product.html', {'data':data, 'query': query})