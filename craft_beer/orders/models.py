from django.db import models
from products.models import Product
from users.models import CustomUser


class Order(models.Model):
    """Модель заказа"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    published = models.DateTimeField(auto_now_add=True, db_index=True)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.id = None

    def __str__(self):
        return f'Заказ {self.id} для {self.user.username}'


class OrderItem(models.Model):
    """Модель элементов заказа"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.amount} x {self.product.name} в заказе {self.order.id}'
