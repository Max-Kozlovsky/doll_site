from django.shortcuts import render


def index(request):
    return render(request, 'home.html')


def main(request):
    return render(request, 'home.html')


def interier_dolls(request):
    return render(request, 'interier_dolls.html')


def for_game(request):
    return render(request, 'game_dolls.html')


def dress(request):
    return render(request, 'dress.html')


def contacts(request):
    return render(request, 'contacts.html')


""""--------------------------------------Модели интерьерных кукол---------------------------------------------------"""


def school(request):
    return render(request, 'school.html')


def longleg(request):
    return render(request, 'longleg.html')


def angel(request):
    return render(request, 'angel.html')


def cool_girl(request):
    return render(request, 'cool_girl.html')


def butterfly(request):
    return render(request, 'butterfly.html')
