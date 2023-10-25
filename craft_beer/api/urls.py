from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import CustomUserViewSet
from products.views import ProductViewSet
from orders.views import OrderViewSet
from cart.views import CartViewSet

router_v1 = DefaultRouter()
router_v1.register(r'users', CustomUserViewSet, basename='user')
router_v1.register(r'products', ProductViewSet, basename='product')
router_v1.register(r'orders', OrderViewSet, basename='order')
router_v1.register(r'carts', CartViewSet, basename='cart')


urlpatterns = [
    path('api/v1/', include(router_v1.urls)),
]
