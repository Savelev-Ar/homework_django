from django.urls import path

from catalog.views import ProductListView, ProductDetailView, ContactsTemplateView

from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogDeleteView, BlogUpdateView


app_name = 'students_list'

urlpatterns = [
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('', ProductListView.as_view(), name='catalog'),
    path('blog/create/', BlogCreateView.as_view(), name='create_blog'),
    path('blog/detail/<int:pk>', BlogDetailView.as_view(), name='detail_blog'),
    path('blog/update/<int:pk>', BlogUpdateView.as_view(), name='update_blog'),
    path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='delete_blog'),
    path('blog/', BlogListView.as_view(), name='list_blog')
]
