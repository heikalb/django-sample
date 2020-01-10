from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, LostPost
from .forms import PostForm, LostForm
from django.http import Http404

# Create your views here.


def post_detail_view(request, id):
    obj = get_object_or_404(Post, id=id)
    context = {'obj': obj}

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
    form = LostForm()

    if request.method == 'POST':
        form = LostForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            LostPost.objects.create(**form.cleaned_data)

        else:
            print(form.errors)

    context = {
        'form': form
    }

    return render(request, 'posts/post_create.html', context)


def delete_post_view(request, id):
    obj = get_object_or_404(LostPost, id=id)

    if request.method == 'POST':
        # confirming delete
        obj.delete()
        return redirect('../../../')

    context = {'obj': obj}

    return render(request, 'posts/post_delete.html', context)


def post_list_view(request):
    queryset = LostPost.objects.all()

    context = {'object_list': queryset}

    return render(request, 'posts/post_list.html', context)