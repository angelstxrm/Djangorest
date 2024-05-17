from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.pk} {self.title}'
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



class Product(models.Model):
    title = models.CharField('Название товара', max_length=100, unique=True)
    description = models.TextField('Описание товара')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, help_text=25000)
    quantity = models.PositiveIntegerField('Количество', default=0)
    image = models.ImageField(upload_to='images/', null=True)
    is_published = models.BooleanField('Опубликовано', default=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f'{self.pk} {self.title}'
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'