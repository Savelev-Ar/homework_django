from django.urls import path

from catalog.views import contacts, product, catalog

app_name = 'students_list'

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', product, name='product'),
    path('catalog/', catalog, name='catalog')
]
