from django.urls import path
from . import views

app_name = 'carts'

urlpatterns = [
    path('', views.cart_home, name='cart_home'),
    path('update', views.cart_update, name='update_cart'),
    path('checkout', views.checkout_home, name='checkout_home'),
    path('api_cart/', views.cart_detail_api_view, name='api-cart')
]