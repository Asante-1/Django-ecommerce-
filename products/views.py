from django.shortcuts import render, redirect,get_object_or_404
from .models import Product
from .forms import ContactForm
from django.http import Http404
from django.contrib.auth import authenticate, login, get_user_model
from django.views.generic import DetailView, ListView
from carts.models import Cart

from django.views.generic import ListView,DetailView
# Create your views here.

def productlistview(request):
    productlist = Product.objects.all()
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    context = {
    'object_list': productlist,
    'cart' : cart_obj,
    }


    return render(request, 'products/product_list.html', context)

class ProductDetailView(DetailView):

    queryset = Product.objects.all()
    template_name = 'products/product_detail.html'


    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('product_slug')
        instance = Product.objects.get_by_slug(slug)
        if instance is None:
            raise Http404('Product does not exist')
        return instance




def product_detail_view(request, product_slug, *args, **kwargs):

    querysetdeatil = Product.objects.get(slug=product_slug)


    if querysetdeatil is None:
        raise Http404('Product does not exist. Sorry such product is not available')


    # qs = Product.objects.filter(slug=product_slug)
    # if qs.count() == 1:
    #     querysetdeatil = qs.first()
    # else:
    #     raise Http404('Product does not exist')

    context = {
        'object': querysetdeatil
               }
    return render(request, 'products/product_detail.html', context)

# def productd(request):
#     productdetail = Product.objects.all()
#     cart_obj, new_obj = Cart.objects.new_or_get(request)
#
#     context = {
#         'productdetail' : productdetail,
#         'cart': cart_obj
#     }
#
#     return render(request, 'products/product_detail.html', context)

def home(request):
    context = {
        'title' : 'Hello world',
        'content' : "welcome to the homepage.",

    }

    if request.user.is_authenticated:
         context["premium_content"] = "YEAHHH"

    return render(request, 'home_page.html', context)

def contact(request):
    contact_form = ContactForm(request.POST or None)

    context = {
        'title' : 'Hello world',
        'content' : "welcome to the contactpage.",
        'form' : contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    return render(request, 'contact_page.html', context)



