from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.forms import inlineformset_factory
from catalog.models import Product, Version
from catalog.forms import ProductForm, VersionForm


class ProductListView(LoginRequiredMixin, ListView):
    login_url = 'users:login'
    redirect_field_name = 'redirect_to'
    model = Product
    fields = ('name', 'description', 'preview')

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        product_list = context_data.get('object_list')
        context_data['version'] = {}
        for product in product_list:
            version = Version.objects.filter(is_current_version=True, product_id=product.pk).first()
            product.version = version
        return context_data


class ProductDetailView(LoginRequiredMixin, DetailView):
    login_url = 'users:login'
    redirect_field_name = 'redirect_to'
    model = Product
    form_class = ProductForm


class ContactsTemplateView(TemplateView):
    template_name = 'contacts.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = 'users:login'
    redirect_field_name = 'redirect_to'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list_product')

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        context_data['formset'] = VersionFormset()
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST)
        else:
            context_data['formset'] = VersionFormset()
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        if form.is_valid():
            new_product = form.save()
            new_product.owner = self.request.user
            new_product.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users:login'
    redirect_field_name = 'redirect_to'
    model = Product
    form_class = ProductForm

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        context_data['formset'] = VersionFormset()
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:detail_product', args=[self.kwargs.get('pk')])


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    model = Product
    success_url = reverse_lazy('catalog:list_product')
