from django.shortcuts import render

from product.models import Product, ProductImage, SliderProduct

# Create your views here.

def index(request):
    slider_products = SliderProduct.objects.all()
    context = {
        "slider_products": slider_products
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

def product_detail(request,slug):
    product_list = Product.objects.all()
    images = ProductImage.objects.all()
    context = {
        'products' : product_list,
        'images' : images,
    }
    return render(request, "products.html", context)