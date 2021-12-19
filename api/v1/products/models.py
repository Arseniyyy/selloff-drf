from io import BytesIO
from PIL import Image

from django.db import models
from django.urls import reverse
from django.core.files import File

from selloff_drf.config import HOST


class Category(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255, db_index=True)
    slug = models.SlugField(verbose_name='Slug', unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return f'/{self.slug}/'

    def __str__(self) -> str:
        return self.name

    
class Product(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255)
    slug = models.SlugField(verbose_name='Slug')
    description = models.TextField(verbose_name='Description', blank=True, null=True)
    price = models.DecimalField(verbose_name='Price', decimal_places=2, max_digits=6)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated at', auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    def get_absolute_url(self) -> str:
        return f'/{self.category.slug}/{self.slug}'

    def get_image(self) -> str:
        if self.image:
            return f'{HOST}/{self.image.url}'

    def get_thumbnail(self):
        if self.thumbnail:
            return f'{HOST}/{self.thumbnail.url}'
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
            else:
                return

    def make_thumbnail(self, image, size=(300, 300)) -> File:
        """
        Makes a thumbnail of the given image.
        """
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)
        return thumbnail

    def __str__(self) -> str:
        return self.name
