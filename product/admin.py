from django.contrib import admin

from product.models import Product, ProductImage, SliderProduct

# Register your models here.

admin.site.register(SliderProduct)
admin.site.register(ProductImage)

admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','category')
    prepopulated_fields = {"slug": ("product_name",)}  # new