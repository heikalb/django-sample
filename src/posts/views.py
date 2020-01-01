from django.shortcuts import render
from .models import Post
from .forms import PostForm
# Create your views here.

def post_detail_view(request):
    obj = Post.objects.get(id=4)
    context = {
                'obj': obj,
                'title' : obj.title,
                'description': obj.description,
                'award': obj.award,
                'contact': obj.contact}

    return render(request, 'posts/post_detail.html', context)


def post_create_view(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()
        form.PostForm()

    context = {
                'form': form}

    return render(request, 'posts/post_create.html', context)