from django.shortcuts import render
from .forms import Order


def index(request):
    return render(request, 'home.html')


def main(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


def send_order(request):
    form = Order(request.POST)
    return render(request, 'order.html', {'form': form})
