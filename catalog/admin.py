from django.contrib import admin

from catalog.models import Product, Category, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Version)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'number_version', 'name', 'is_current_version')
    list_filter = ('product',)
    search_fields = ('name', 'number_version')
