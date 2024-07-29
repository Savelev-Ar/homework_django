from django.shortcuts import render

from catalog.models import Product


def contacts(request):
    return render(request, 'contacts.html')


def catalog(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list
    }
    return render(request, 'products.html', context)


def product(request):
    product = Product.objects.get(name='коробокс')
    context = {
        'object': product
    }
    return render(request, 'product.html', context)
