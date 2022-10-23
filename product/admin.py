from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from product.models import Category, Product, ProductImage, SliderProduct

# Register your models here.
admin.site.register(SliderProduct)
admin.site.register(ProductImage)

# admin.site.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('product_name','category')
#     prepopulated_fields = {"slug": ("product_name",)}  # new


    
@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    group_fieldsets = True  
    list_display = ('product_name',)
    prepopulated_fields = {"slug": ("product_name",),}
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
        
@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    group_fieldsets = True  
    list_display = ('name',)
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
