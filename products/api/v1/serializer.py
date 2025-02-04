from rest_framework import serializers
from products.models import Product


class ProductModelSerializer(serializers.Serializer):

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('id',)
        fields = ['id', 'title', 'description', 'price', 'image']
