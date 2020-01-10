from django.shortcuts import render
from posts.models import Post
# Create your views here.


def home_view(request, *args, **kwargs):
    print(request.user)

    queryset = Post.objects.all()

    context = {'posts': queryset}

    return render(request, 'home.html', context)
