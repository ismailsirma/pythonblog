from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

# Create your views here.
def post_create(request):
    return HttpResponse("<h1>Create</h1>")

def post_detail(request):
    context = {
        "title": "Detail"
    }
    return render(request,"index.html",context) # context as an empty dictionary
    #return HttpResponse("<h1>Detail</h1>")

def post_list(request):

    queryset = Post.objects.all()
    context = {
        "object_list":queryset,
        "title":"List",
    }
    # if request.user.is_authenticated():
    #     context = {"title": "My User List"}
    #     #return render(request,"index2.html",context)
    # else:
    #     context = {"title": "List"}
    return render(request,"index.html",context) # context as an empty dictionary
    #return HttpResponse("<h1>List</h1>")

def post_update(request):
    return HttpResponse("<h1>Update</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")