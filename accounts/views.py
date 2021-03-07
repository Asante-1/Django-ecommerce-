from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, GuestForm
from django.contrib.auth import authenticate, login, get_user_model
from django.views.generic import DetailView
from carts.models import Cart
from .models import GuestEmail

from django.utils.http import is_safe_url

# Create your views here.

User = get_user_model()


def register_page(request):
    reg_form = RegisterForm(request.POST or None)
    context = {
        'form': reg_form,
    }
    if reg_form.is_valid():
        # print(reg_form.cleaned_data)
        username = reg_form.cleaned_data.get('username')
        email = reg_form.cleaned_data.get('email')
        password = reg_form.cleaned_data.get('password')
        new_user = User.objects.create_user(username, email, password)

    return render(request, 'accounts/register.html', context)

def login_page(request):

    form_login = LoginForm(request.POST or None)
    context = {
        'form': form_login,
    }

    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None

    # print("User logged in")
    # print(request.user.is_authenticated)
    if form_login.is_valid():
        username = form_login.cleaned_data.get('username')
        password = form_login.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                context['form'] = LoginForm()

            return redirect('products:home')
        else:
            print("Errors")


    return render(request, 'accounts/login.html', context)


def guest_login_view(request):

    form_login = GuestForm(request.POST or None)
    context = {
        'form': form_login,
    }

    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None


    if form_login.is_valid():

        email = form_login.cleaned_data.get('email')
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id

        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect('accounts:register')

    return redirect('accounts:register')