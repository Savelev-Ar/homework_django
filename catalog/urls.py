from django.urls import path

from catalog.views import contacts, home

app_name = 'students_list'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
]
