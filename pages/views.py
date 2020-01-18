from django.shortcuts import render
from posts.models import Post
# Create your views here.


def home_view(request):
    """
    View for homepage.
    :param request: request object
    :return:
    """
    queryset = Post.objects.all()
    context = {'posts': queryset}

    return render(request, 'home.html', context)
