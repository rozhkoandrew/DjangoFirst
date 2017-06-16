from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello , if you want to create blog - go to the admin panel")