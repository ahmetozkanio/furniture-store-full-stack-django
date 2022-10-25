from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation

from product.models import Product


def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        # if view.url_name == 'product_detail':
        #    next_url = Product.get_absolute_url(view.url_name,view.args)
       
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
        

    else:
        response = HttpResponseRedirect("/")
    return response