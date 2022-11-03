from modeltranslation.translator import  TranslationOptions, register

from pages.models import About




@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('description',)

