from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from core.models import Product, Category
from core.serializers import ProductSerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        slug = self.kwargs.get('slug')  # берём slug из URL
        if slug:
            # находим категорию по slug и фильтруем товары
            queryset = queryset.filter(category__slug=slug)
        return queryset