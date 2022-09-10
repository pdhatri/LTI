from django.http import HttpResponse
from django.shortcuts import render

# Created views for display of content when user clicks on the link.
def index(request):
    return HttpResponse("Welcome to Computer Education Class")