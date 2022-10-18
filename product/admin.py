from django.contrib import admin

from product.models import Product, ProductImage

# Register your models here.


admin.site.register(ProductImage)
admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','category')