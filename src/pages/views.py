from django.shortcuts import render
from posts.models import LostPost
# Create your views here.


def home_view(request):
    """
    View for homepage.
    :param request: request object
    :return:
    """
    queryset = LostPost.objects.all()
    context = {'posts': queryset}

    return render(request, 'home.html', context)
