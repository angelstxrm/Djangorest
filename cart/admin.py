from django.contrib import admin
from .models import Cart, CartItem

class CartItemAdmin(admin.TabularInline):
    model = CartItem
    list_display = ('product', 'cart', 'created_at')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'total_quantity')
    inlines = [CartItemAdmin]


