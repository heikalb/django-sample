from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, LostPost, FoundPost
from .forms import PostForm, LostForm, FoundForm, DeleteForm
from django.core.files.storage import default_storage
from django.http import Http404

# Create your views here.


# For viewing individual posts
def post_detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    context = {'post': post}

    return render(request, 'posts/post_detail.html', context)


# For viewing multiple posts (to be extended)
def post_list_view(request, PostClass, heading):
    queryset = PostClass.objects.all()
    context = {'posts': queryset, 'heading': heading}

    return render(request, 'posts/post_list.html', context)


# For viewing lost pet posts (LostPost class)
def lost_post_list_view(request):
    return post_list_view(request, LostPost, 'Lost pets')


# For viewing found pet posts (FoundPost class)
def found_post_list_view(request):
    return post_list_view(request, FoundPost, "Pets people found")


# For creating posts (to be extended)
def post_create_view(request, PostClass, FormClass, heading):
    form = FormClass()
    response_msg = ''
    new_post = None

    if request.method == 'POST':
        form = FormClass(request.POST, request.FILES)

        if form.is_valid():
            new_post = PostClass.objects.create(**form.cleaned_data)
            form = FormClass()
            response_msg = 'Your post has been created'
        else:
            print(form.errors)

    context = {'form': form,
               'heading': heading,
               'response_msg': response_msg,
               'new_post': new_post}

    return render(request, 'posts/post_create.html', context)


# For creating lost pet posts
def lost_post_create_view(request):
    return post_create_view(request, LostPost, LostForm, 'Report a lost pet')


# For creating found pet posts
def found_post_create_view(request):
    return post_create_view(request, FoundPost, FoundForm, 'Report a pet you found')


# For reference only (not used in webapp)
def post_create_view_(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()
        form.PostForm()

    context = {'form': form}

    return render(request, 'posts/post_create.html', context)


def delete_post_view(request, id):
    post = get_object_or_404(Post, id=id)
    form = DeleteForm()
    response_msg = ''

    if request.method == 'POST':
        if post.password == request.POST['password']:
            if post.picture:
                default_storage.delete(post.picture.path)

            post.delete()
            return redirect('/')
        else:
            response_msg = 'Incorrect password'

    context = {'post': post, 'form': form, 'response_msg': response_msg, }

    return render(request, 'posts/post_delete.html', context)
