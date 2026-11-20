from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def catalog(request):
    return render(request, 'main/catalog.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def favorites(request):
    return render(request, 'main/favorites.html')