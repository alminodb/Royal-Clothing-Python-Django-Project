from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    categorynames = CategoryName.objects.all()
    categories = Category.objects.all()
    products = Product.objects.all()


    context = {
        'categorynames':categorynames,
        'categories':categories,
        'products':products,
    }
    return render(request, 'index.html', context)


def details(request, id, size="default"):
    product = Product.objects.get(id = id)
    sizes = ProductSize.objects.all()

    images = ProductImages.objects.all()

    context = {
        'product' : product,
        'sizes':sizes,
        'size':size,
        'images':images,
    }
    return render(request, 'details.html', context)


def cart(request):
    return render(request, 'cart.html')