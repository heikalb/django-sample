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
def post_list_view(request, PostClass):
    queryset = PostClass.objects.all()
    context = {'posts': queryset}

    return render(request, 'posts/post_list.html', context)


# For viewing lost pet posts (LostPost class)
def lost_post_list_view(request):
    return post_list_view(request, LostPost)


# For viewing found pet posts (FoundPost class)
def found_post_list_view(request):
    return post_list_view(request, FoundPost)


# For creating base post (just for reference)
def post_create_view(request, PostClass, FormClass):
    form = FormClass()

    if request.method == 'POST':
        form = FormClass(request.POST)

        if form.is_valid():
            PostClass.objects.create(**form.cleaned_data)
            form = FormClass()
        else:
            print(form.errors)

    context = {'form': form}

    return render(request, 'posts/post_create.html', context)


# For creating lost pet posts
def lost_post_create_view(request):
    return post_create_view(request, LostPost, LostForm)


# For creating found pet posts
def found_post_create_view(request):
    return post_create_view(request, FoundPost, FoundForm)


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
