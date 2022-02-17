from rest_framework import serializers
from django.utils.text import slugify

from v1.products.models import Category, Product
    

class ProductDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'slug',
            'description',
            'price',
            'image',
            'thumbnail',
            'category',
            'is_active'
        ]


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'slug',
            'description',
            'price',
            'image',
            'thumbnail',
            'category',
            'is_active',
        ]

class ProductListRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'slug',
            'description',
            'price',
            'category',
            'is_active',
            'get_image',
            'get_thumbnail',
            'get_absolute_url_api',
            'get_absolute_url_client'
        ]


class CategorySerializer(serializers.ModelSerializer):
    products = ProductListRetrieveSerializer(many=True)

    class Meta:
        model = Category
        fields = [
            'slug',
            'products'
        ]
