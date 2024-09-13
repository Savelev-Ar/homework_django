from config.settings import CACHE_ENABLED
from django.core.cache import cache
from catalog.models import Category


def get_category():

    if not CACHE_ENABLED:
        return Category.objects.all()
    key = "category_list"
    categories = cache.get(key)
    if categories is not None:
        return categories
    categories = Category.objects.all()
    cache.set(key, categories)
    return categories
