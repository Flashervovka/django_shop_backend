from rest_framework.permissions import AllowAny  # или IsAuthenticated, если нужно
from rest_framework import viewsets
from ..models import Category
from ..serializers import CategorySerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]  # публичный каталог
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
