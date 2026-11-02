from django.urls import path

from .views import product_list, category_list

urlpatterns = [
    # Важно: без префикса /api/, потому что главный urls.py уже добавляет /api/
    path('products/', product_list, name='product-list'),
    path('categories/', category_list, name='category-list'),
]