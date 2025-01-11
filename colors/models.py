from django.db import models
from products.base_models import BaseModel


class Color(BaseModel):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

