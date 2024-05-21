from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from .forms import LoginUserForm, RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = LoginUserForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("users:login"))

def users_home(request):
    return render(request, 'users_home.html')

def home_page(request):
    return render(request, 'home_page.html')




