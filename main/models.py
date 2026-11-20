from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse

from pathlib import Path

# Create your models here.

def product_image_path(instance, filename):
    ext = Path(filename).suffix
    slug = instance.slug or "product"
    return f"product/{slug}/{slug}{ext}"

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:category', kwargs={'slug': self.slug})

class Brand(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:brand', kwargs={'slug': self.slug})

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    article = models.CharField(max_length=50, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to=product_image_path, blank=True)
    count = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new and not self.article:
            br = ((self.brand.slug or "")[:3] or "BRD").upper()
            cat = ((self.category.slug or "")[:3] or "CAT").upper()
            self.article = f"{br}-{cat}-{self.pk:05d}"
            super().save(update_fields=['article'])

    def get_absolute_url(self):
        return reverse('main:product', kwargs={'slug': self.slug})
