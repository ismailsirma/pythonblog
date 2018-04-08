# added by reloaded 07.04.2018

from django.shortcuts import render

def home(request):
    # context is a  python dictionary.
    context = {}
    template = "home.html"
    return render(request,template,context)

