from django.urls import path

from catalog.views import ProductListView, ProductDetailView, ContactsTemplateView

app_name = 'students_list'

urlpatterns = [
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('', ProductListView.as_view(), name='catalog')
]
