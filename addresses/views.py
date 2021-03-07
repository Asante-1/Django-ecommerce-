from django.shortcuts import render, redirect
from .forms import AddressForm
from django.utils.http import is_safe_url
from billing.models import BillingProfile
# Create your views here.

def checkout_address_create_view(request):
    form_address = AddressForm(request.POST or None)
    context = {
        'forms': form_address,
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None

    if form_address.is_valid():
        print(request.POST)
        instance = form_address.save(commit=False)

        billing_profile, billing_guest_profile_create = BillingProfile.objects.new_or_get(request)
        if billing_profile is not None:

            address_type = request.POST.get('address_type', 'shipping')
            instance.billing_profile = billing_profile
            instance.address_type = address_type
            instance.save()

            request.session[address_type + "_address_id"] = instance.id
            print(address_type + "_address_id")
        else:
            return redirect('carts:checkout_home')
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect('carts:checkout_home')
    return redirect('carts:checkout_home')


