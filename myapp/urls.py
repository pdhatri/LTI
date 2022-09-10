from django.urls import path

from . import views

#include the path where user needs to get redirected to when clicked on a link
urlpatterns=[
    path('',views.index,name='index'),
]