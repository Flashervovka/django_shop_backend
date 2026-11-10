from django.db import models
from django.utils.text import slugify
from unidecode import unidecode

from core.models.categories import Category


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products'
    )
    name = models.CharField('Название', max_length=200)
    slug = models.SlugField('Слаг', unique=True, blank=True)
    description = models.TextField('Описание', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    image = models.ImageField('Картинка товара', upload_to='products/', blank=True, null=True)  # ← добавили
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        # Генерация слага, если его нет
        if not self.slug and self.name:
            base_slug = slugify(unidecode(self.name))
            slug = base_slug
            counter = 1
            while Product.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = slug

        # Удаление старой картинки, если она была заменена
        if self.pk:
            try:
                old_instance = Product.objects.get(pk=self.pk)
                if old_instance.image and self.image != old_instance.image:
                    old_instance.image.delete(False)
            except Product.DoesNotExist:
                pass

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} — {self.price} ₽'