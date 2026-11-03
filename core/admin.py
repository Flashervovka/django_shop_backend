
from django.contrib import admin
from django.utils.html import format_html
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image_preview')
    prepopulated_fields = {'slug': ('name',)}
    # УБРАЛИ readonly_fields = ('slug',) — это и вызывало ошибку

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" />', obj.image.url)
        return 'Нет изображения'

    image_preview.short_description = 'Превью'