from django.contrib import admin
from .models import Cart, CartItem


from django.contrib import admin
from .models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price') 
    inlines = [CartItemInline] 

    def total_price(self, obj):
        return obj.total_price()
    total_price.short_description = 'Общая сумма'

admin.site.register(Cart, CartAdmin)