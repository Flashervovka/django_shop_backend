from django.contrib import admin
from django.utils.html import format_html
from django.db import models

from core.admin.widgets import AdminImageWidget
from core.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'is_active', 'image_preview', 'created_at')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'description')
    list_editable = ('price', 'stock', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-created_at',)
    autocomplete_fields = ['category']

    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget},
    }

    @admin.display(description='Фото')
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" />', obj.image.url)
        return 'Нет фото'