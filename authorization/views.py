from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm,ProfileForm
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone_number = form.cleaned_data.get('phone_number')
            Profile.objects.create(user=user, phone_number=phone_number)
            messages.success(request, f'Аккаунт создан для {user.email}!')
            login(request, user)
            return redirect('authorization:profile')
    else:
        form = UserRegisterForm()
    return render(request, 'main/index.html', {'register_form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('authorization:profile')
    else:
        form = UserLoginForm()
    return render(request, 'auth/login.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('authorization:profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'auth/profile.html', {'form': form})