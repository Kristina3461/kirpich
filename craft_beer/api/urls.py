from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import CustomUserViewSet
from products.views import ProductViewSet
from orders.views import OrderViewSet, OrderItemViewSet
from cart.views import CartViewSet, CartItemViewSet

router_v1 = DefaultRouter()
router_v1.register(r'users', CustomUserViewSet, basename='user')
router_v1.register(r'products', ProductViewSet, basename='product')
router_v1.register(r'orders', OrderViewSet, basename='order')
router_v1.register(r'order-items', OrderItemViewSet, basename='order-item')
router_v1.register(r'carts', CartViewSet, basename='cart')
router_v1.register(r'cart-items', CartItemViewSet, basename='cart-item')

urlpatterns = [
    path('api/v1/', include(router_v1.urls)),
]
