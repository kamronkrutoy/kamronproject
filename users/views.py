from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.urls import reverse
from users.forms import UserRegistrationForm, UserLoginForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(request, username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect(reverse('myapp:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Home Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return redirect(reverse('user:login'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Home Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', context)

def profile(request) -> HttpResponse:
    context = {
        'title': 'Home Кабинет'
    }
    return render(request, 'users/profile.html', context)

def logout(request) -> HttpResponse:
    auth.logout(request)
    return redirect(reverse('main:index'))
