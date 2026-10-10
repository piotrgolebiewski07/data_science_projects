from django.shortcuts import render
from django.http import HttpResponse


# ta funkcja musi się nazywać dokładnie tak jak w pliku urls.py
def iris_home(request):
    return HttpResponse("witaj w projekcie klasyfikacji kwiatów iris!")
