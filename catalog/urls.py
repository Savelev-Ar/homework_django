from django.urls import path

from catalog.views import contacts, products

app_name = 'students_list'

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', products, name='products')
]
