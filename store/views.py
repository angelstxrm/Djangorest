from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from drf_spectacular.utils import extend_schema_view, extend_schema


from .serializers import ProductsListSerializer, ProductsCreateSerializer
from .models import Product

@extend_schema_view(
    get=extend_schema(summary='Просмотр всех продуктов', tags=['Продукты магазина']),
)

class ProductsListView(generics.ListAPIView):
    serializer_class = ProductsListSerializer

    def get_queryset(self):
        products = Product.objects.all()
        return products

@extend_schema_view(
    get=extend_schema(summary='Просмотр продуктов по ID', tags=['Продукты магазина']),
)

class ProductsDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(is_published=True)
    serializer_class = ProductsListSerializer

    
@extend_schema_view(
    post=extend_schema(summary='Создание продукта', tags=['Продукты магазина']),
)
class ProductsCreateView(generics.CreateAPIView):
    serializer_class = ProductsCreateSerializer
