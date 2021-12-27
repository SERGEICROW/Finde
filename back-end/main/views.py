
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

import requests

# Create your views here.
from django.views.generic import ListView

from .forms import *
from .models import UserProfile, Product


def home(request):
    # data = request.user.userprofile.address
    # address = list(UserProfile.objects.values('id', 'address'))

    # ids = [t[0] for t in UserProfile.objects.values_list('id', 'address')]
    # data2 = [i[1] for i in UserProfile.objects.values_list('id', 'address')]
    # coords = []
    #
    #
    # # GEOCODE API
    # API_KEY = 'Mi clave de API'
    #
    # for i in data2:
    #     params = {
    #         'key': API_KEY,
    #         'address': i
    #     }
    #
    #     base_url = "https://maps.googleapis.com/maps/api/geocode/json?"
    #     response = requests.get(base_url, params=params).json()
    #     response.keys()
    #
    #     if response['status'] == 'OK':
    #         geometry = response['results'][0]['geometry']
    #         lat = geometry['location']['lat']
    #         lng = geometry['location']['lng']
    #
    #         coords.append([lat, lng])
    #
    # context = {
    #     'coords': coords,
    #     'data': data
    # }

    return render(request, "home.html",{})


def signPage(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data['username']
            messages.success(request, 'Tu cuenta fue creada ' + user)
            return redirect('log')
        else:
            messages.info(request, 'Tu usuario ya esta registrado o las contrasenas no son correctas')

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
            messages.success(request, 'Username or Password incorrect')

    context = {}

    return render(request, "log.html", context)


@login_required(login_url='log')
def home_logged(request):
    data = UserProfile.objects.filter(user=request.user)

    context = {
        'data': data
    }

    return render(request, "home_logged.html", context)


@login_required(login_url='log')
def editProfile(request):
    data = UserProfile.objects.filter(user=request.user)

    curpForm = CurpUpdate()
    phoneForm = PhoneUpdate()
    bAddressForm = BAddressUpdate()
    pictureForm = ProfilePicUpdate()

    if request.method == 'POST':
        if request.POST.get("form_type") == 'Update Picture':
            pictureForm = ProfilePicUpdate(request.POST, request.FILES, instance=request.user.userprofile)
            if pictureForm.is_valid():
                pictureForm.save()
                messages.success(request, 'Picture updated!')

        if request.POST.get("form_type") == 'Update Curp':
            curpForm = CurpUpdate(request.POST, instance=request.user.userprofile)
            if curpForm.is_valid():
                curpForm.save()
                messages.success(request, 'Curp updated!')

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
        pictureForm = ProfilePicUpdate()

    context = {'data': data,
               'curpForm': curpForm,
               'phoneForm': phoneForm,
               'bAddressForm': bAddressForm,
               'pictureForm': pictureForm
               }

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
    data = UserProfile.objects.filter(user=request.user)

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
        'productForm': productForm,
        'data': data
    }

    return render(request, "publish.html", context)

def logoutUser(request):
    logout(request)
    return redirect('log')


# TESTING

# Search bar based in classes
class SearchView(ListView):
    model = Product
    template_name = 'test.html'
    context_object_name = 'products'

    def get_queryset(self):
        # result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Product.objects.filter(title__contains=query)
            result = postresult
        else:
            result = None
        return result
