from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.models import Product, Blog



class ProductListView(ListView):
    model = Product
    template_name = 'products.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'


class ContactsTemplateView(TemplateView):
    template_name = 'contacts.html'


class BlogCreateView(CreateView):
    model = Blog
    fields = ('header', 'content', 'preview')
    success_url = reverse_lazy('catalog:list_blog')

class BlogListView(ListView):
    model = Blog
    fields = ('header', 'view_count')

class BlogDetailView(DetailView):
    model = Blog
    fields = ('header', 'content', 'preview')

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('header', 'content', 'preview')
    success_url = reverse_lazy('catalog:list_blog')

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:list_blog')