from django.db import models
from products.models import Product


class Cart(models.Model):
    """Модель для корзины"""
    objects = None
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f'Корзина для {self.user.username}'


class CartItem(models.Model):
    """Модель для элементов в корзине"""
    objects = None
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.product.name} в корзине.'
