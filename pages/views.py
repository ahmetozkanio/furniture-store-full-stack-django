from unicodedata import category
from django.shortcuts import render, redirect
from django.urls import reverse
from pages.models import About, Fair, FairImage
from product.models import Category, CategoryProduct, HeroBottomProduct, Product, ProductCatalogImage, ProductImage, SliderProduct

from django.utils import translation
# Create your views here.

def index(request):
    slider_products = SliderProduct.objects.all()
    hero_bottom_products = HeroBottomProduct.objects.all()
    category_products = CategoryProduct.objects.all()
    context = {
        "slider_products" : slider_products,
        'hero_bottom_products' : hero_bottom_products,
        'category_products':category_products
    }
    return render(request, "index.html", context)

def products(request):
    product_list = Product.objects.all()

    category_list = Category.objects.all()
    
    context = {
        'products' : product_list,

        'category_list' : category_list,
          'category' : 'categorySample',

    }
    return render(request, "products.html", context)

def category_products(request, slug):
    product_list = Product.objects.filter(category__slug=slug)
    category_list = Category.objects.all()
    # category = Category.objects.get(slug = slug)
    # slug = category.get_absolute_url()
    context = {
        'products' : product_list,
        'category_list' : category_list,
        # 'slug' : slug,
        # 'category' : category,
    }
    return render(request, "products.html", context)

def product_detail(request, slug):


    product = Product.objects.get(slug = slug)
    images = ProductImage.objects.all().filter(product = product)
    catalog_images = ProductCatalogImage.objects.all().filter(product = product)
    slug = product.get_absolute_url()

    context = {
        'product' : product,
        'slug' : slug,
        'images' : images,
        'catalog_images' : catalog_images,
    }
    return render(request, "product_detail.html", context)

def about(request):
    about_object = About.objects.all()
    context = {
        "about_object" : about_object,
    }
    return render(request, "about.html", context)

def fair(request):
    fairs = Fair.objects.all()
    context = {
        "fairs" : fairs,
    }
    return render(request, "fairs.html", context)


def fair_detail(request, slug):

    fair = Fair.objects.get(slug = slug)
    images = FairImage.objects.all().filter(fair = fair)

    context = {
        'fair' : fair,
        'images' : images,
    }
    return render(request, "fair_detail.html", context)

def contact(request):
    return render(request, "contact.html")

def catalog(request):
    return render(request, "catalog.html")
