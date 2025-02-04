from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.api.v1.serializer import ProductModelSerializer
from products.models import Product


@api_view(['GET', 'POST'])
def Product_list(request):

    if request.method == 'GET':
        products = Product.objects.all()
        products_serial = ProductModelSerializer(products, many=True, context={'request': request})
        return Response(products_serial.data)

    if request.method == 'POST':
        data = request.data
        products_serial = ProductModelSerializer(data=data)
        products_serial.is_valid(raise_exception=True)
        products_serial.save()
        return Response(products_serial.data)


@api_view(['GET', 'PUT', 'DELETE'])
def Product_list(request):

    products = get_object_or_404(Product, pk=id)
    if request.method == 'GET':
        try:
            products = Product.objects.get(pk=id)
            products_after_serial = ProductModelSerializer(products, context={'request': request})
            return Response(products_after_serial.data)
        except Exception as e:
            return Response({'msg': 'not Found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        data = request.data
        products_after_serial = ProductModelSerializer(products, data=data)
        products_after_serial.is_valid(raise_exception=True)
        products_after_serial.save()
        return Response(products_after_serial.data)

    if request.method == 'DELETE':
        products.delete()