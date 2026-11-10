from django.contrib.admin.widgets import AdminFileWidget
from django.utils.html import format_html

class AdminImageWidget(AdminFileWidget):
    """Виджет с превью текущей картинки над кнопкой загрузки."""
    def render(self, name, value, attrs=None, renderer=None):
        output = super().render(name, value, attrs, renderer)
        if value and getattr(value, 'url', None):
            output = format_html(
                '<img src="{}" width="150" style="display:block; margin-bottom:8px; border-radius:6px;" />',
                value.url
            ) + output
        return output