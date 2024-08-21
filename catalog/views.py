from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from catalog.models import Product
from catalog.forms import ProductForm


class ProductListView(ListView):
    model = Product
    fields = ('name', 'description', 'preview')

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        # queryset = queryset.filter(is_posted=True)
        return queryset


class ProductDetailView(DetailView):
    model = Product
    form_class = ProductForm

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        # self.object.save()
        return self.object

class ContactsTemplateView(TemplateView):
    template_name = 'contacts.html'




class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list_product')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()

            new_product.save()
            return super().form_valid(form)
    def get_success_url(self):
        return reverse('catalog:detail_product', args=[self.kwargs.get('pk')])

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:list_product')