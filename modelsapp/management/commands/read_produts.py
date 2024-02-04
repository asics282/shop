from django.core.management.base import BaseCommand
from modelsapp.models import Product


class Command(BaseCommand):
    help = 'Список всех продуктов'

    def handle(self, *args, **kwargs):
        products = Product.objects.all()

        if products:
            for product in products:
                self.stdout.write(f'Имя: {product.name}, Цена: {product.price}, Количество: {product.quantity}')
        else:
            self.stdout.write(self.style.SUCCESS('Нет доступных продуктов'))
