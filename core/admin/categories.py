from django.contrib import admin
from django.db import models
from django.utils.html import format_html

from core.admin.widgets import AdminImageWidget
from core.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'slug', 'image_preview')
    prepopulated_fields = {'slug': ('name',)}

    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget},
    }

    @admin.display(description='Фото')
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" />', obj.image.url)
        return 'Нет изображения'