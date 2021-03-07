from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'products'


urlpatterns = [
    path('', views.home, name='home'),
    # path('login', views.login_page, name='login'),
    # path('register', views.register_page, name='register'),
    path('bootstrap', TemplateView.as_view(template_name='bootstrap/example.html')),
    path('contact', views.contact, name='contact'),
    path('productlist', views.productlistview, name='productlist'),
    path('<slug:product_slug>', views.ProductDetailView.as_view(), name='product_detail'),
    path('<slug:product_slug>', views.product_detail_view, name='product_detail'),
    # path('<slug:product_slug>', views.ProductDetailView.as_view(), name='productdetailview'),
]