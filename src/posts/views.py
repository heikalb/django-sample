from django.shortcuts import render
from .models import Post
from .forms import PostForm, RawPostForm
# Create your views here.

def post_detail_view(request):
    obj = Post.objects.get(id=4)
    context = {
                'obj': obj,
                'title': obj.title,
                'description': obj.description,
                'award': obj.award,
                'contact': obj.contact}

    return render(request, 'posts/post_detail.html', context)


def post_create_view_(request):
    print(request.GET)
    print(request.GET['title'])
    print(request.POST)

    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()
        form.PostForm()

    context = {'form': form}

    return render(request, 'posts/post_create.html', context)


def post_create_view(request):
    form = RawPostForm()

    if request.method == 'POST':
        form = RawPostForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            Post.objects.create(**form.cleaned_data)

        else:
            print(form.errors)

    context = {
        'form': form
    }

    return render(request, 'posts/post_create.html', context)
