from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    path('login', views.login_page, name='login'),
    path('register', views.register_page, name='register'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('guestregister', views.guest_login_view, name='guest'),

]
