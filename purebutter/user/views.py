from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SigninForm
from .models import CustomUser


def sign_in(request):

    form = SigninForm(request.POST or None)

    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        sent = True
        new_user = CustomUser.objects.create_user(email, password)
        new_user.save()
        return redirect('home')

    return render(request, 'user/signin.html', locals())


def log_in(request):

    form = SigninForm(request.POST or None)

    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request=request, user=user)
            logged = True
            return(redirect("home"))
        else:
            logged = False

    return render(request, 'user/login.html', locals())


def log_out(request):

    logout(request)
    return redirect("home")