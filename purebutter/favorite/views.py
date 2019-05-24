from django.shortcuts import render, redirect, HttpResponse

from products.models import Product

from .models import UserFavorite

def add_favorite(request):
    print(request.POST)
    if request.user.is_authenticated:
        new_favorite = UserFavorite(user=request.user,
                                    to_substitute=Product.objects.get(pk=request.POST["to_substitute"]),
                                    substitution=Product.objects.get(pk=request.POST["substitution"])
                                    )
        new_favorite.save()
    else:
        redirect('home')

    return redirect('fav_list')

def fav_list(request):
    all_favorites = UserFavorite.objects.filter(user=request.user)

    return render(request, 'favorite/favorite_page.html', locals())

#TODO: Finish to add_favorite view
#TODO : Finish favorite_page.html