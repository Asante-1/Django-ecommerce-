from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'addresses'


urlpatterns = [
    path('checkout_address', views.checkout_address_create_view, name='checkout_address_create '),

]