from django.db.models.signals import pre_delete
from django.dispatch import receiver
from core.models import Product, Category

@receiver(pre_delete, sender=Product)
def delete_product_image(sender, instance, **kwargs):
    """Удаляет файл изображения товара перед удалением объекта."""
    if instance.image:
        # delete(False) означает "не сохранять изменения в БД", нам нужно только удалить файл
        instance.image.delete(False)

@receiver(pre_delete, sender=Category)
def delete_category_image(sender, instance, **kwargs):
    """Удаляет файл изображения категории перед удалением объекта."""
    if instance.image:
        instance.image.delete(False)