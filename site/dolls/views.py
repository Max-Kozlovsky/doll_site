from django.shortcuts import render
from .models import InteriorDolls, PlayDolls, Toys

"""_________________________________Interior Dolls___________________________________________________________________"""


def interior_dolls_list(request):
    dolls = InteriorDolls.objects.all()
    context = {
        'dolls': dolls
    }
    return render(request, 'interior_dolls_list.html', context)


def interior_doll_detail(request, pk):
    doll = InteriorDolls.objects.get(pk=pk)
    context = {
        'doll': doll
    }
    return render(request, 'interior_detail.html', context)


"""-------------------------------Game dolls-------------------------------------------------------------------------"""


def for_game_list(request):
    play_dolls = PlayDolls.objects.all()
    context = {
        'play_dolls': play_dolls
    }
    return render(request, 'for_game_list.html', context)


def for_game_detail(request, pk):
    play_doll = PlayDolls.objects.get(pk=pk)
    context = {
        'play_doll': play_doll
    }
    return render(request, 'for_game_detail.html', context)


"""--------------------------------------Toys------------------------------------------------------------------------"""


def toys_list(request):
    toys = Toys.objects.all()
    context = {
        'toys': toys
    }
    return render(request, 'toys_list.html', context)


def toys_detail(request, pk):
    toy = Toys.objects.get(pk=pk)
    context = {
        'toy': toy
    }
    return render(request, 'toy_detail.html', context)
