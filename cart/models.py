from django.db import models
from django.contrib.auth.models import User
from store.models import Product  

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_price = models.DecimalField('Общая сумма', max_digits=32, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Cart of {self.user.username}"
    
    def update_total_price(self):
        total = sum(item.product.price * item.quantity for item in self.items.all())
        self.total_price = total
        self.save()
    
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.title} in {self.cart.user.username}'s cart"

    class Meta:
        verbose_name = 'Корзина (Детальная запись)'
        verbose_name_plural = 'Корзина (Детальные записи)'