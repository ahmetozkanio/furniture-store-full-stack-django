from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from pages.models import About,Fair,FairImage

# Register your models here.


@admin.register(About)
class AboutAdmin(TranslationAdmin):
    group_fieldsets = True  
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class FairImagesAdmin(admin.StackedInline):
    model = FairImage    

@admin.register(Fair)
class FairAdmin(TranslationAdmin):
    group_fieldsets = True  
    inlines = [FairImagesAdmin]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }