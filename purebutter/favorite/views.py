from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from products.models import Product

from .models import UserFavorite


@login_required(login_url="login")
def add_favorite(request):
    new_favorite = UserFavorite(user=request.user,
                                to_substitute=Product.objects.get(pk=request.POST["to_substitute"]),
                                substitution=Product.objects.get(pk=request.POST["substitution"])
                                )
    new_favorite.save()

    return redirect('fav_list')


@login_required(login_url="login")
def fav_list(request):
    all_favorites = UserFavorite.objects.filter(user=request.user)

    return render(request, 'favorite/favorite_page.html', locals())

#TODO: Finish to add_favorite view
#TODO : Finish favorite_page.html