# added by ismailsirma 07.04.2018
from django.http import HttpResponse
from django.shortcuts import render

def post_home(request):
    return HttpResponse("<h1>Hello!</h1>")