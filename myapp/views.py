from django.http import HttpResponse
from django.shortcuts import render

# Created views for display of content when user clicks on the link.
def index(request):
    #retrieved course id and user name to display
    return HttpResponse("Welcome user: "+request.POST["custom_canvas_course_id"]+" to the course with id: "+ request.POST["custom_canvas_user_id"])