from django.http import HttpResponse
from django.shortcuts import render
from .models import Pizza


def index(request):
    pizzas = Pizza.objects.all().order_by("prix")
    noPrix = 5
    # pizzas_names_and_prices = [pizza.nom + ": " + str(pizza.prix) + " $" for pizza in pizzas]
    # pizza_name_price = (", ").join(pizzas_names_and_prices)
    # return HttpResponse("Les pizzas: " + pizza_name_price)
    return render(request,'menu/index.html',{
        'pizzas' : pizzas
    })