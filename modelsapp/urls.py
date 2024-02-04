from django.urls import path
from .views import OrderListView, create_product, HomeView

urlpatterns = [
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('create_product/', create_product, name='create_product'),
    path('', HomeView.as_view(), name='home'),
]
