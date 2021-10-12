import base64
import platform

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

from .forms import SignUpForm, CurpUpdate, PhoneUpdate, BAddressUpdate, NewProduct
from .models import UserProfile, Product


def home(request):
    return render(request, "home.html", {})


def signPage(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data['username']
            # user = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + user)

            return redirect('log')

    context = {'form': form}

    return render(request, 'sign.html', context)


def logPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_logged')
        else:
            messages.info(request, 'Username or Password incorrect')
    context = {}

    return render(request, "log.html", context)


@login_required(login_url='log')
def home_logged(request):
    return render(request, "home_logged.html", {})


@login_required(login_url='log')
def editProfile(request):
    data = UserProfile.objects.filter(user=request.user)
    curpForm = CurpUpdate()
    phoneForm = PhoneUpdate()
    bAddressForm = BAddressUpdate()

    if request.method == 'POST':
        if request.POST.get("form_type") == 'Update Curp':
            curpForm = CurpUpdate(request.POST, instance=request.user.userprofile)
            if curpForm.is_valid():
                curpForm.save()
                messages.success(request, 'Curp updated!')
                return redirect('edit_profile')

        elif request.POST.get("form_type") == 'Update Phone':
            phoneForm = PhoneUpdate(request.POST, instance=request.user.userprofile)
            if phoneForm.is_valid():
                phoneForm.save()
                messages.success(request, 'Phone updated!')

        elif request.POST.get("form_type") == 'Update Address':
            bAddressForm = BAddressUpdate(request.POST, instance=request.user.userprofile)
            if bAddressForm.is_valid():
                bAddressForm.save()
                messages.success(request, 'Address updated!')
    else:
        curpForm = CurpUpdate()
        phoneForm = PhoneUpdate()
        bAddressForm = BAddressUpdate()

    context = {'data': data,
               'curpForm': curpForm,
               'phoneForm': phoneForm,
               'bAddressForm': bAddressForm}

    return render(request, "edit_profile.html", context)


@login_required(login_url='log')
def editLists(request):
    productData = Product.objects.filter(user=request.user)

    context = {
        'productData': productData
    }

    return render(request, "edit_lists.html", context)


@login_required(login_url='log')
def publish(request):
    # productForm = NewProduct(request.POST,)
    #
    # if productForm.is_valid():
    #     p = productForm.save(commit=False)
    #     p.user = (request.user)
    #     p.save()
    #     messages.success(request, 'Product added')
    #     return redirect('edit_lists')
    # else:
    #     print('error')

    if request.method == 'POST':
        productForm = NewProduct(request.POST, request.FILES)
        if productForm.is_valid():
            p = productForm.save(commit=False)
            p.user = (request.user)
            p.save()
            return redirect('edit_lists')
    else:
        productForm = NewProduct()

    context = {
        'productForm': productForm
    }

    return render(request, "publish.html", context)


@login_required(login_url='log')
def test(request):
    productData = Product.objects.filter(user=request.user)

    context = {
        'productData': productData
    }
    return render(request, "test.html", context)


def logoutUser(request):
    logout(request)
    return redirect('log')

