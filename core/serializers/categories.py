
from rest_framework import serializers
from ..models import Category


class CategorySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'image']

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None