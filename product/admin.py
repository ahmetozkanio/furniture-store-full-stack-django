from django.contrib import admin

from product.models import Product

# Register your models here.


admin.site.register(Product)

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('product_name','category')