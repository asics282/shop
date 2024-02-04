from django.core.management.base import BaseCommand
from modelsapp.models import Product


class Command(BaseCommand):
    help = 'Create a new product'

    def handle(self, *args, **kwargs):
        name = input('Введите имя: ')
        description = input('Ввведите описание: ')
        price = float(input('Введите цену: '))
        quantity = int(input('Введите количество: '))

        Product.objects.create(
            name=name,
            description=description,
            price=price,
            quantity=quantity
        )

        self.stdout.write(self.style.SUCCESS('Продукт успешно создан'))
