from django.urls import path, include, re_path
from posts import views
# from posts import post_view # class based view
from . import views

urlpatterns = [
    re_path(r'^$', views.post_list), # first url to be matched
    re_path(r'^create/$', views.post_create), # function based view added
    re_path(r'^detail/$', views.post_detail), #
    re_path(r'^update/$', views.post_update), #
    re_path(r'^delete/$', views.post_delete), #
]