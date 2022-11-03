from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from product.models import Category, CategoryProduct, HeroBottomProduct, Product, ProductCatalogImage, ProductImage, SliderProduct

# Register your models here.

admin.site.register(HeroBottomProduct)
admin.site.register(SliderProduct)
admin.site.register(ProductImage)

# admin.site.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('product_name','category')
#     prepopulated_fields = {"slug": ("product_name",)}  # new

class ProductImagesAdmin(admin.StackedInline):
    model = ProductImage 
class ProductCatalogImagesAdmin(admin.StackedInline):
    model = ProductCatalogImage    
@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    group_fieldsets = True  
    inlines = [ProductImagesAdmin,ProductCatalogImagesAdmin]
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
    prepopulated_fields = {"slug": ("name",),}
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(CategoryProduct)
class CategoryProductAdmin(TranslationAdmin):
    group_fieldsets = True  
    list_display = ('product',)
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }