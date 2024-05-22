from rest_framework import viewsets, permissions
from drf_spectacular.utils import extend_schema_view, extend_schema

from .serializers import ProductSerializer
from .models import Product

@extend_schema_view(
    list=extend_schema(summary='Просмотр всех продуктов', tags=['Продукты магазина']),
    update=extend_schema(summary='Изменение продукта', tags=['Продукты магазина']),
    create=extend_schema(summary='Создание продукта', tags=['Продукты магазина']),
    retrieve=extend_schema(summary='Детальный просмотр продукта', tags=['Продукты магазина']),
    destroy=extend_schema(summary='Удаление продукт', tags=['Продукты магазина']),
)

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'put', 'delete']