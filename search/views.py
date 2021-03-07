from django.shortcuts import render, redirect
from products.models import Product
from django.db.models import Q

def search_productlist_view(request):
    queryset = Product.objects.all()


    search_query = request.GET.get('q', None)
    if search_query:
        queryset = queryset.filter(
            Q(title__icontains = search_query) |
            Q(description__icontains = search_query)|
            Q(price__icontains = search_query)|
            Q(tag__title__icontains = search_query)

    ).distinct()


    context = {
        'object_list': queryset
    }

    return render(request, 'search/product_list.html', context)