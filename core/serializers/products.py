from rest_framework import serializers
from core.models import Product

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    category_slug = serializers.CharField(source='category.slug', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'slug',
            'name',
            'description',
            'price',
            'stock',
            'is_active',
            'category',
            'category_name',
            'image',
            'created_at',
            'category_slug'
        ]
        read_only_fields = ['slug', 'category_name', 'created_at']