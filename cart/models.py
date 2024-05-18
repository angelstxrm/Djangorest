from django.db import models
from django.contrib.auth import get_user_model
from store.models import Product


User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=32, decimal_places=2, default=0)
    total_quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
     

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name = 'Корзина (Детальная запись)'
        verbose_name_plural = 'Корзина (Детальные записи)'