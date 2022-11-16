from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello(request):
    return HttpResponse("<h1> Hola Magola </h1>")

def notasdjango(request):
    return HttpResponse("<h1>Respondo desde la función notasdjango en el archivo views de la app cineapp</h1>")