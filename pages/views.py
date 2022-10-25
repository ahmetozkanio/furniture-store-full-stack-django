from django.shortcuts import render, redirect
from django.urls import reverse
from product.models import Product, ProductImage, SliderProduct

from django.utils import translation
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

def product_detail(request, slug):

    cur_language = translation.get_language()





    product = Product.objects.get(slug = slug)
    print('HELLOOOOO')
    print(slug)
    images = ProductImage.objects.all().filter(product = product)
    
    # languages = dict(settings.LANGUAGES).keys()
    # q = Q()
    # for lang in languages:
    #     kwargs = {'slug_%s' % lang: slug}
    #     q |= Q(**kwargs)
    # articles = Product.objects.filter(slug = slug)
    # if articles.exists():
    #     article = articles.first()
    # else:
    #     return Http404
    # return reverse('product_detail', kwargs={'slug': slug})
    context = {
        'product' : product,
        'images' : images,
    }
    return render(request, "product_detail.html", context)

