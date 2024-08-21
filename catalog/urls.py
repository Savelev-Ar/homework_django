from django.urls import path

from catalog.views import (ProductCreateView, ProductListView, ProductDetailView, ProductUpdateView, ProductDeleteView,
                           ContactsTemplateView)

from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogDeleteView, BlogUpdateView


app_name = 'product_list'

urlpatterns = [
    path('', ProductListView.as_view(), name='list_product'),
    path('product/create/', ProductCreateView.as_view(), name='create_product'),
    path('product/update/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='detail_product'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path('blog/create/', BlogCreateView.as_view(), name='create_blog'),
    path('blog/detail/<int:pk>', BlogDetailView.as_view(), name='detail_blog'),
    path('blog/update/<int:pk>', BlogUpdateView.as_view(), name='update_blog'),
    path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='delete_blog'),
    path('blog/', BlogListView.as_view(), name='list_blog'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts')
]
