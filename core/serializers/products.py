from rest_framework import serializers
from ..models import Product

class ProductSerializer(serializers.ModelSerializer):
    # Добавляем читаемое имя категории, чтобы фронтенду не пришлось делать второй запрос
    category_name = serializers.CharField(source='category.name', read_only=True)

    # Если хочешь также отдавать всю категорию объектом (не только имя), раскомментируй строку ниже:
    # category_detail = CategorySerializer(source='category', read_only=True)

    class Meta:
        model = Product
        # Важно: включаем slug, так как он нужен для красивых URL на фронтенде
        fields = [
            'id',
            'slug',
            'name',
            'description',
            'price',
            'stock',
            'is_active',
            'category',  # ID категории (для POST/PUT запросов)
            'category_name',  # Имя категории (только для чтения)
            'created_at'
        ]
        # read_only_fields можно вынести сюда, но для slug логика уже в модели,
        # а category_name мы и так сделали read_only через source.
        read_only_fields = ['slug', 'category_name', 'created_at']