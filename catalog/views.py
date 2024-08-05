from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product



class ProductListView(ListView):
    model = Product
    template_name = 'products.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'


class ContactsTemplateView(TemplateView):
    template_name = 'contacts.html'
def contacts(request):
    return render(request, 'contacts.html')

