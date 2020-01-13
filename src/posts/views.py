from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, LostPost, FoundPost
from .forms import PostForm, LostForm, FoundForm
from django.http import Http404

# Create your views here.


# For viewing individual posts
def post_detail_view(request, id):
    obj = get_object_or_404(Post, id=id)
    context = {'obj': obj}

    return render(request, 'posts/post_detail.html', context)


# For viewing multiple posts (to be extended)
def post_list_view(request):
    queryset = Post.objects.all()
    context = {'posts': queryset}

    return render(request, 'posts/post_list.html', context)


# For viewing lost pet posts (LostPost class)
def lost_post_list_view(request):
    queryset = LostPost.objects.all()
    context = {'posts': queryset}

    return render(request, 'posts/post_list.html', context)


# For viewing found pet posts (FoundPost class)
def found_post_list_view(request):
    queryset = FoundPost.objects.all()
    context = {'posts': queryset}

    return render(request, 'posts/post_list.html', context)


# For creating base post (just for reference)
def post_create_view(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
            form = PostForm
        else:
            print(form.errors)

    context = {'form': form}

    return render(request, 'posts/post_create.html', context)


# For creating lost pet posts
def lost_post_create_view(request):
    form = LostForm()

    if request.method == 'POST':
        form = LostForm(request.POST)

        if form.is_valid():
            LostPost.objects.create(**form.cleaned_data)
            form = LostForm()
        else:
            print(form.errors)

    context = {'form': form}

    return render(request, 'posts/post_create.html', context)


# For creating found pet posts
def found_post_create_view(request):
    form = FoundForm()

    if request.method == 'POST':
        form = FoundForm(request.POST)

        if form.is_valid():
            FoundPost.objects.create(**form.cleaned_data)
            form= FoundForm()
        else:
            print(form.errors)

    context = {'form': form}

    return render(request, 'posts/post_create.html', context)


# For reference only (not used in webapp)
def post_create_view_(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()
        form.PostForm()

    context = {'form': form}

    return render(request, 'posts/post_create.html', context)






def delete_post_view(request, id):
    obj = get_object_or_404(LostPost, id=id)

    if request.method == 'POST':
        # confirming delete
        obj.delete()
        return redirect('../../../')

    context = {'obj': obj}

    return render(request, 'posts/post_delete.html', context)
