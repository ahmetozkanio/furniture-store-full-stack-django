from django.contrib import admin
from django.urls import include, path
from pages import views
from django.utils.translation import gettext_lazy as _
from django.conf.urls import *
urlpatterns = [
    path('',views.index,name = "index" ),
    path(_('urunler/'),views.products,name = "products" ),
    path(_('urunler/<slug:slug>'),views.product_detail,name = "product_detail" ),
    
]

