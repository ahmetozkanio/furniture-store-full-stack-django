from django.contrib import admin
from django.urls import include, path
from pages import views
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import *

urlpatterns = [
    path('',views.index,name = "index" ),
    path(_('urun/<slug:slug>'),views.product_detail, name = "product_detail" ),
    path(_('urunler/'),views.products,name = "products" ),
    path(_('urunler/<slug:slug>'),views.category_products,name = "category_products" ),
    # path(_('urunler/<int:id>'),views.category_products,name = "category_products" ),

    path(_('hakkimizda'),views.about,name = "about" ),
    path(_('fuarlar'),views.fair,name = "fairs" ),
    path(_('fuar/<slug:slug>'),views.fair_detail,name = "fair_detail" ),
    path(_('iletisim'),views.contact,name = "contact" ),
]


