from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Django index page from mysite.views!")