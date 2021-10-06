from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import SignUpForm, UserProfileForm


def test(request):
    return render(request, "test.html", {})


def home(request):
    return render(request, "home.html", {})


def signPage(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # profile_form = UserProfileForm(request.POST)

        if form.is_valid():
            form.save()
            # profile_form.save(commit=False)
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
def profileEdit(request):
    return render(request, "profile.html", {})


def logoutUser(request):
    logout(request)
    return redirect('log')
