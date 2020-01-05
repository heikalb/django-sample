"""django_sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact_view
from posts.views import post_detail_view, post_create_view, dynamic_lookup_view, delete_post_view, post_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('posts/', post_detail_view, name='post'),
    path('create/', post_create_view, name='create-post'),
    path('posts/<int:id>', dynamic_lookup_view, name='post'),
    path('posts/<int:id>/delete/', delete_post_view, name='post-delete'),
    path('post-list/', post_list_view, name='post-list')
]
