from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):

        Category.objects.all().delete()

        category_list = [
            {'name': 'фрукты'},
            {'name': 'овощи', 'description': 'можно кушать'},
            {'name': 'мясо', 'description': 'вкуснее овощей'},
            {'name': 'игровые консоли', 'description': 'можно играть'}
        ]

        category_for_create = []
        for category in category_list:
            category_for_create.append(
                Category(**category)
            )

        Category.objects.bulk_create(category_for_create)
