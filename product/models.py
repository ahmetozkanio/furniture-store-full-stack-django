
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse 
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
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
    slug = models.SlugField(blank =True,null = True, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_products", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Product(models.Model):

    # class Categories(models.TextChoices):
    #     MasaTakımı = 'MasaT', _('Masa Takımı')
    #     Masa = 'Masa', _('Masa')
    #     Sandalye = 'Sandalye', _('Sandalye')        
    #     OrtaSehpa = 'OrtaS', _('Orta Sehpa')
    #     YanSehpa = 'YanS', _('Yan Sehpa')
    #     ServisSehpası = 'ServisS', _('Servis Sehpası')
    #     SetSehpa = 'SetS', _('Set Sehpa')
    #     Puf = 'Puf', _('Puf')

    product_name = models.CharField(max_length = 256, null = True, unique=True)
    category = models.ForeignKey(Category, on_delete =models.CASCADE, null = True)
    # category = models.CharField(max_length=8,choices=Categories.choices,blank =True, null = True)
    description = RichTextField(null = True)
    image = models.ImageField(upload_to ='product/image/%Y/%m/%d/',null = True)
    slug = models.SlugField(blank =True,null = True, unique=True)
    
    def __str__(self):
        return self.product_name
    
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})

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