from django.shortcuts import render, get_object_or_404
from .models import Product
from .models import Product1
from .models import Product2
from .models import Product3
from .models import Product4
from django.http import Http404

def home(request):
    return render(request,'base.html')

def animal(request):
    products3 = Product3.objects.all()
    context = {
        'products3': products3
    }
    return render(
        request,
        'pages/animal.html',
        context
    )

def animal_detail(request,pk):
    try:
        product3 = Product3.objects.get(id=pk)
    except Product3.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'product3': product3
    }

    return render(request, 'pages/animal_detail.html', context)


def business(request):
    products1 = Product1.objects.all()
    context = {
        'products1': products1
    }
    return render(
        request,
        'pages/business.html',
        context
    )

def business_detail(request,pk):
    try:
        product1 = Product1.objects.get(id=pk)
    except Product1.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'product1': product1
    }

    return render(request, 'pages/business_detail.html', context)

def electro(request):
    products2 = Product2.objects.all()
    context = {
        'products2': products2
    }
    return render(
        request,
        'pages/electro.html',
        context
    )

def electro_detail(request,pk):
    try:
        product2 = Product2.objects.get(id=pk)
    except Product2.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'product2': product2
    }

    return render(request, 'pages/electro_detail.html', context)

def realty(request):
    return render(request, 'pages/realty.html')

def furnature(request):
    products4 = Product4.objects.all()
    context = {
        'products4': products4
    }
    return render(
        request,
        'pages/furnature.html',
        context
    )

def furnature_detail(request,pk):
    try:
        product4 = Product4.objects.get(id=pk)
    except Product4.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'product4': product4
    }

    return render(request, 'pages/furnature_detail.html', context)

def transport(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(
        request,
        'pages/transport.html',
        context
    )

def transport_detail(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'product': product
    }

    return render(request, 'pages/transport_detail.html', context)

#*args, **kwargs





