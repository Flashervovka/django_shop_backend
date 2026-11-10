from django.db import models
from django.utils.text import slugify
from unidecode import unidecode


class Category(models.Model):
    name = models.CharField('Название', max_length=255)
    slug = models.SlugField('Слаг', unique=True, blank=True)
    image = models.ImageField('Изображение', upload_to='categories/', blank=True, null=True)
    description = models.TextField('Описание', blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            base_slug = slugify(unidecode(self.name))
            slug = base_slug
            counter = 1
            while Category.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = slug
        # Удаление старой картинки, если она была заменена
        if self.pk:
            try:
                old_instance = Category.objects.get(pk=self.pk)
                if old_instance.image and self.image != old_instance.image:
                    old_instance.image.delete(False)
            except Category.DoesNotExist:
                pass


        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
