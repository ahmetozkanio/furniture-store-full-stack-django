from django.contrib import admin
from django.urls import include, path
from pages import views

urlpatterns = [
    path('',views.index,name = "index" ),
    path('products/',views.products,name = "products" ),
    path('products/<slug:slug>',views.product_detail,name = "product_detail" ),

]