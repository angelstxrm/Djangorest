from rest_framework.response import Response
from rest_framework import viewsets

from drf_spectacular.utils import extend_schema_view, extend_schema

from .serializers import ProductSerializer

from .models import Product

# @extend_schema_view(
#     get=extend_schema(summary='Просмотр всех продуктов', tags=['Продукты магазина']),
# )

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer