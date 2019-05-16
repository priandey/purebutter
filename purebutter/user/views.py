from django.shortcuts import render
from .forms import SigninForm
from .models import CustomUser

def signin(request):

    form = SigninForm(request.POST or None)

    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        sent = True
        new_user = CustomUser.objects.create_user(email, password)
        new_user.save()

    return render(request, 'user/signin.html', locals())

# Create your views here.
