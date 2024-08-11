from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

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

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.header)
            new_blog.save()
            return super().form_valid(form)

class BlogListView(ListView):
    model = Blog
    fields = ('header', 'view_count')

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_posted=True)
        return queryset

class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('header', 'content', 'preview')
    #success_url = reverse_lazy('catalog:list_blog')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.header)
            new_blog.save()
            return super().form_valid(form)
    def get_success_url(self):
        return reverse('catalog:detail_blog', args=[self.kwargs.get('pk')])

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:list_blog')