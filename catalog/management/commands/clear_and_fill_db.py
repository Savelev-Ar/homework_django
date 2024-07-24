from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category_list = [
            {'pk': 1, 'name': 'овощи', 'description': 'можно кушать'},
            {'pk': 2, 'name': 'фрукты'},
            {'pk': 3, 'name': 'мясо', 'description': 'вкуснее овощей'},
            {'pk': 4, 'name': 'игровые консоли', 'description': 'можно играть'}
        ]

        category_for_create = []
        for category in category_list:
            category_for_create.append(
                Category(**category)
            )
        Category.objects.bulk_create(category_for_create)

        products_list = [
            {'name': 'помидор', 'description': 'синьор', 'category': Category.objects.get(pk=1), 'price': 10},
            {'name': 'огурец', 'description': 'молодец', 'category': Category.objects.get(pk=1), 'price': 5},
            {'name': 'яблоко', 'description': 'наливные', 'category': Category.objects.get(pk=2), 'price': 15},
            {'name': 'апельсин', 'description': 'оранжевый', 'category': Category.objects.get(pk=2), 'price': 20},
            {'name': 'говядина', 'category': Category.objects.get(pk=3), 'price': 10},
            {'name': 'свинина', 'category': Category.objects.get(pk=3), 'price': 10},
            {'name': 'коробокс', 'description': 'не забудь подписка', 'category': Category.objects.get(pk=4),
             'price': 2000}
        ]

        products_for_create = []
        for product in products_list:
            products_for_create.append(
                Product(**product)
            )
        Product.objects.bulk_create(products_for_create)
