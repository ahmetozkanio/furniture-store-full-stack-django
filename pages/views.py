from django.shortcuts import render, redirect
from django.urls import reverse
from product.models import HeroBottomProduct, Product, ProductImage, SliderProduct

from django.utils import translation
# Create your views here.

def index(request):
    slider_products = SliderProduct.objects.all()
    hero_bottom_products = HeroBottomProduct.objects.all()
    context = {
        "slider_products" : slider_products,
        'hero_bottom_products' : hero_bottom_products
    }
    return render(request, "index.html", context)

def products(request):
    product_list = Product.objects.all()
    images = ProductImage.objects.all()
    context = {
        'products' : product_list,
        'images' : images,
    }
    return render(request, "products.html", context)

def product_detail(request, slug):

    cur_language = translation.get_language()


    product = Product.objects.get(slug = slug)
    images = ProductImage.objects.all().filter(product = product)
    slug = product.get_absolute_url()

    context = {
        'product' : product,
        'slug' : slug,
        'images' : images,
    }
    return render(request, "product_detail.html", context)

