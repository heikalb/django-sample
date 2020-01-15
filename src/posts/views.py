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
def post_list_view(request, PostClass, heading):
    queryset = PostClass.objects.all()
    context = {'posts': queryset, 'heading': heading}

    return render(request, 'posts/post_list.html', context)


# For viewing lost pet posts (LostPost class)
def lost_post_list_view(request):
    heading = 'Lost pets'
    return post_list_view(request, LostPost, heading)


# For viewing found pet posts (FoundPost class)
def found_post_list_view(request):
    heading = "Pets other people found"
    return post_list_view(request, FoundPost, heading)


# For creating posts (to be extended)
def post_create_view(request, PostClass, FormClass, heading):
    form = FormClass()
    response_msg = ''

    if request.method == 'POST':
        form = FormClass(request.POST, request.FILES)

        if form.is_valid():
            PostClass.objects.create(**form.cleaned_data)
            form = FormClass()
            response_msg = 'Your post has been created'
        else:
            print(form.errors)

    context = {'form': form, 'heading': heading, 'response_msg': response_msg}

    return render(request, 'posts/post_create.html', context)


# For creating lost pet posts
def lost_post_create_view(request):
    heading = 'Report a lost pet'
    return post_create_view(request, LostPost, LostForm, heading)


# For creating found pet posts
def found_post_create_view(request):
    heading = 'Report a pet you found'
    return post_create_view(request, FoundPost, FoundForm, heading)


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
