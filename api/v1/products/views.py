from django.http.response import Http404
from django.utils.text import slugify
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework import status
from rest_framework.decorators import api_view
from django.db.models import Q

from v1.products.serializers import (CategorySerializer,
                                     ProductListRetrieveSerializer,
                                     ProductDestroySerializer,
                                     ProductCreateSerializer)
from v1.products.models import Category, Product


class ProductListCreateAPIView(APIView):
    """
    * Lists all products
    * Creates a new product
    * Deletes all products
    """
    serializer_class = ProductCreateSerializer

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductListRetrieveSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request: Request, format=None):
        data = request.data.copy()
        data.__setitem__('slug', slugify(data.get('name')))
        serializer = ProductCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        """Deletes all the products in the database."""
        products = Product.objects.all()
        products.delete()
        return Response(products)


class ProductDetailAPIView(APIView):
    """Gets detailed information about a certain product."""
    serializer_class = ProductListRetrieveSerializer

    def get_object(self, category_slug: str, product_slug: str):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug: str, product_slug: str, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductListRetrieveSerializer(product)
        return Response(serializer.data)


class CategoryDetailAPIView(APIView):
    def get_object(self, category_slug: str):
        try:
            return Category.objects.get(slug=category_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug: str, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


@api_view(['POST'])
def search(request: Request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query)
                                          | Q(slug__icontains=query)
                                          | Q(description__icontains=query))
        serializer = ProductListRetrieveSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response('No products found')
