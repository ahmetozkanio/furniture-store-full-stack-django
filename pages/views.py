from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "numbers": [1, 2, 3, 4, 5, 6]
    }
    return render(request, "index.html", context)