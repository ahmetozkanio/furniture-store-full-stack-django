from django.db import models

# Create your models here.




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



class Product(models.Model):
    product_name = models.CharField(max_length = 256,null = True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=6)
    description = models.TextField(blank =True,null = True)
    image = models.ImageField(upload_to ='product/image/%Y/%m/%d/',null = True)
    slug = models.SlugField( blank =True,null = True)
    def __str__(self):
        return self.product_name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='product_image', on_delete= models.CASCADE)
    image = models.ImageField(upload_to ='product/images/%Y/%m/%d/')
    def __str__(self):
        return self.product.product_name


class SliderProduct(models.Model):
    product = models.ForeignKey(Product,related_name='slider_product', on_delete=models.CASCADE)
    def __str__(self):
        return self.product.product_name