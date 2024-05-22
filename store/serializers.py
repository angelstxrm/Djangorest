from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    # Валидация на цену.
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError('Price must be greater than 0')
        return value