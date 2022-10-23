
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse 
# Create your models here.




# CATEGORY_CHOICES = (
#     ('MT','Masa Takımı'),
#     ('M', 'Masa'),
#     ('S', 'Sandalye'),
#     ('OS', 'Orta Sehpa'),
#     ('YS', 'Yan Sehpa'),
#     ('SES', 'Servis Sehpası'),
#     ('SS', 'Set Sehpa'),
#     ('P', 'Puf'),
# )


class Category(models.Model):
    name = models.CharField(max_length = 256, null = True)
    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length = 256, null = True, unique=True)
    # category = models.CharField(choices=CATEGORY_CHOICES, max_length=6)
    category = models.OneToOneField(Category,on_delete=models.CASCADE,related_name='category', null = True)
    description = models.TextField(blank =True,null = True)
    image = models.ImageField(upload_to ='product/image/%Y/%m/%d/',null = True)
    slug = models.SlugField(blank =True,null = True, unique=True)
    
    def __str__(self):
        return self.product_name
    
    def get_absolute_url(self):
        return reverse("a", kwargs={"slug": self.slug})

    # Product url icin otomatik ismi alir slug yerine yazar.
    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.product_name)
        return super().save(*args, **kwargs)



class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='product_image', on_delete= models.CASCADE)
    image = models.ImageField(upload_to ='product/images/%Y/%m/%d/')
    def __str__(self):
        return self.product.product_name


class SliderProduct(models.Model):
    product = models.ForeignKey(Product,related_name='slider_product', on_delete=models.CASCADE)
    def __str__(self):
        return self.product.product_name

class HeroBottomProduct(models.Model):
    product = models.ForeignKey(Product,related_name='hero_bottom_product', on_delete=models.CASCADE)
    def __str__(self):
        return self.product.product_name