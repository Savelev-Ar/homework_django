from django.shortcuts import render

from catalog.models import Product


def contacts(request):
    return render(request, 'contacts.html')


def products(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list
   }
    return render(request, 'products.html', context)
