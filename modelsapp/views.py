from django.shortcuts import render, redirect
from django.views import View
from .models import Order, Client, Product
from .forms import ProductForm


class OrderListView(View):
    template_name = 'modelsapp/orders.html'

    def get(self, request, *args, **kwargs):
        # Создаем несколько клиентов
        client1 = Client.objects.create(name='Pavel', email='pavel@example.com', phone_number='123-456-7890',
                                        address='Moscow', reg_data='2022-01-01')
        client2 = Client.objects.create(name='Stas', email='stas@example.com', phone_number='987-654-3210',
                                        address='Omsk', reg_data='2022-01-02')

        # Создаем несколько продуктов
        product1 = Product.objects.create(name='Цепь 1', description='Описание 1', price=1200, quantity=10,
                                          added_date='2022-01-01')
        product2 = Product.objects.create(name='Цепь 2', description='Описание 2', price=800, quantity=20,
                                          added_date='2022-01-02')
        product3 = Product.objects.create(name='Цепь 3', description='Описание 3', price=500, quantity=15,
                                          added_date='2022-01-03')

        # Создаем несколько заказов
        order1 = Order.objects.create(client=client1, total_amount=2000)
        order1.products.set([product1, product2])

        order2 = Order.objects.create(client=client2, total_amount=1000)
        order2.products.set([product2, product3])

        orders = Order.objects.all()
        return render(request, self.template_name, {'orders': orders})


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('order_list')  # пока перенаправление на страницу с списком заказов
    else:
        form = ProductForm()
    return render(request, 'modelsapp/create_product.html', {'form': form})


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html', {'greeting': 'Вас приветствует, Asics28'})
