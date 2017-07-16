from django.http import HttpResponse

def index(request):
    return HttpResponse ("Reached the correct app") 
