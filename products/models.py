from django.db import models
from .base_models import BaseModel
from colors.models import Color
from catalogs.models import Catalog
from brands.models import Brand


class Product(BaseModel):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='product_image/')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

