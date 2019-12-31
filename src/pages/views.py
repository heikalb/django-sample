from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, 'home.html', {})
    #return HttpResponse("<h1>Welcome!</h1>")


def contact_view(request, *args, **kwargs):
    return HttpResponse('<h1>Contact page</h1>')