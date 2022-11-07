from modeltranslation.translator import  TranslationOptions, register

from pages.models import About,Fair




@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Fair)
class FairTranslationOptions(TranslationOptions):
    fields = ('name','description',)