from django.shortcuts import render


def index(request):
    return render(request, 'CutenessOverload/index.html')

def details(request):
    return render(request,'CutenessOverload/details.html')