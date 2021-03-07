from django.urls import path
from .views import search_productlist_view

app_name = 'search'
urlpatterns = [
    path('searchproductlist', search_productlist_view, name='searchproductlist'),
]