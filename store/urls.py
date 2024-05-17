from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductsListView.as_view()),
    path('products/<int:pk>/', ProductsDetailView.as_view()),
    path('products/create/', ProductsCreateView.as_view()),
]