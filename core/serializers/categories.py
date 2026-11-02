from rest_framework import serializers
from ..models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категории — пригодится, если захочешь отдавать вложенную структуру."""
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']