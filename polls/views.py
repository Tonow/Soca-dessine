from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Soča je t'aime! :heart:")
