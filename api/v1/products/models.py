from io import BytesIO
from PIL import Image
from os import path

from django.db import models
from django.urls import reverse
from django.core.files import File
from django.utils.text import slugify

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
    description = models.TextField(verbose_name='Description', max_length=500, blank=True, null=True, default='No description')
    price = models.DecimalField(verbose_name='Price', decimal_places=2, max_digits=6)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', default='images/default.png', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='images/%Y/%m/%d/', default='images/default.png', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated at', auto_now=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name='Is active', default=True)

    class Meta:
        ordering = ['-created_at']

    def get_absolute_url_api(self) -> str:
        return path.join(HOST, 'api', 'v1', 'products', self.category.slug, self.slug)

    def get_absolute_url_client(self) -> str:
        return path.join(HOST, 'products', self.category.slug, self.slug)

    def get_image(self) -> str:
        if self.image:
            return f'{HOST}{self.image.url}'

    def get_thumbnail(self):
        if self.thumbnail:
            return f'{HOST}{self.thumbnail.url}'
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
