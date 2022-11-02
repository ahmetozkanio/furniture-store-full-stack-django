from modeltranslation.translator import  TranslationOptions, register
from .models import Category, CategoryProduct, Product



@register(CategoryProduct)
class CategoryProductTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name', 'description','slug')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name','slug')

