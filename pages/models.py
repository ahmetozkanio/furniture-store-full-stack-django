from django.db import models

from product.models import Product

# Create your models here.

class SliderProduct(models.Model):
    product = models.ForeignKey(Product,related_name='slider_product', on_delete=models.CASCADE)
    def __str__(self):
        return self.product.product_name