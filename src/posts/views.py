from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm, RawPostForm
from django.http import Http404

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


def dynamic_lookup_view(request, id):
    # obj = Post.objects.get(id=id)
    obj = get_object_or_404(Post, id=id)

    """
    try:
        obj = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404
    """
    context = {'obj': obj}

    return render(request, 'posts/post_detail.html', context)


def delete_post_view(request, id):
    obj = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        # confirming delete
        obj.delete()
        return redirect('../../../')

    context = {'obj': obj}

    return render(request, 'posts/post_delete.html', context)

