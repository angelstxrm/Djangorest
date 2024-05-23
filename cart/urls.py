from django.urls import path
from .views import (
    CartListCreateView,
    CartRetrieveUpdateDestroyView,
    CartItemCreateView,
    CartItemRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('carts/', CartListCreateView.as_view(), name='cart-list-create'),
    path('carts/<int:pk>/', CartRetrieveUpdateDestroyView.as_view(), name='cart-retrieve-update-destroy'),
    path('cart-items/', CartItemCreateView.as_view(), name='cart-item-create'),
    path('cart-items/<int:pk>/', CartItemRetrieveUpdateDestroyView.as_view(), name='cart-item-retrieve-update-destroy'),
]
