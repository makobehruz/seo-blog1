from django.db import models
from django.urls import reverse
from brands.models import Brand
from categories.models import Category
from colors.models import Color
from .base_model import BaseModel
from django.utils.text import slugify


class Product(BaseModel):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='products')
    desc = models.TextField()
    image = models.ImageField(upload_to='products_image')
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_detail_url(self):
        return reverse('products:detail', args=[
            self.pk,
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])

    def get_delete_url(self):
        return reverse('products:delete', args=[self.pk])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

class Comment(BaseModel):
    name = models.CharField(max_length=100)
    rating = models.CharField(max_length=50)
    review = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.name




