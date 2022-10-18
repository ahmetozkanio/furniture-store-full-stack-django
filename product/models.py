from django.db import models

# Create your models here.


# CATEGORY_CHOICES = (
#     ('MT', 'Table Set','Masa Takımı'),
#     ('M', 'Table','Masa'),
#     ('S', 'Sandalye','Chair'),
#     ('OS', 'Orta Sehpa','Middle Coffee Table'),
#     ('OS', 'Servis Sehpası','Service Coffee Table'),
#     ('SS', 'Set Sehpa','Set Coffee Table'),
    
# )
CATEGORY_CHOICES = (
    ('MT','Masa Takımı'),
    ('M', 'Masa'),
    ('S', 'Sandalye'),
    ('OS', 'Orta Sehpa'),
    ('YS', 'Yan Sehpa'),
    ('SES', 'Servis Sehpası'),
    ('SS', 'Set Sehpa'),
    ('P', 'Puf'),
)

# class Chair(models.Model):
#     chair_name = models.CharField(max_length= 128)
#     chair_name = models.CharField(max_length= 128)


class Product(models.Model):
    product_name = models.CharField(max_length = 256,null = False)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=6,null = True)
    description = models.TextField(null = True)
    slug = models.SlugField( null = True)
    def __str__(self):
        return self.product_name

# class ProductImage(models.Model):
#     product = models.ImageField(upload_to ='')
