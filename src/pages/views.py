from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)

    context = {
        'text': 'Hello, I am a text',
        'number': 24,
        'birds': ['sparrows', 'juncos', 'hummingbirds'],
        'do_display': False
    }

    return render(request, 'home.html', context)


def contact_view(request, *args, **kwargs):
    return HttpResponse('<h1>Contact page</h1>')