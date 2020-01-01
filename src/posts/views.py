from django.shortcuts import render
from .models import Post
# Create your views here.

def post_detail_view(request):
    obj = Post.objects.get(id=3)

    context = {'title' : obj.title,
               'description': obj.description,
               'award': obj.award,
               'contact': obj.contact}

    return render(request, 'post/detail.html', context)
