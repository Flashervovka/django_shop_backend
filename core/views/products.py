from rest_framework.permissions import AllowAny  # или IsAuthenticated, если нужно
from rest_framework import viewsets
from ..models import Product
from ..serializers import ProductSerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]  # публичный каталог
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
