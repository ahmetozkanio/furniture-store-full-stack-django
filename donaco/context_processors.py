
from product.models import Category


def context_categories(request):
    return {
        "context_categories": Category.objects.all()
    }