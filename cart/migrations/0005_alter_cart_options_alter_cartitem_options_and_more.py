# Generated by Django 5.0.6 on 2024-05-23 06:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_cart_options_alter_cartitem_options_and_more'),
        ('store', '0007_alter_product_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзины'},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name': 'Корзина (Детальная запись)', 'verbose_name_plural': 'Корзина (Детальные записи)'},
        ),
        migrations.AddField(
            model_name='cartitem',
            name='total_amount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='total_amount', to='store.product', to_field='price'),
        ),
    ]
