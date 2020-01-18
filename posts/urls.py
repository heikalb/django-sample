from django.urls import path

from .views import (
    post_detail_view,
    lost_post_list_view,
    found_post_list_view,
    lost_post_create_view,
    found_post_create_view,
    delete_post_view,
    post_list_view
)

urlpatterns = [
    path('<int:id>', post_detail_view, name='post-detail'),

    path('', post_list_view, name='post-list'),
    path('lost/', lost_post_list_view, name='lost-post-list'),
    path('found/', found_post_list_view, name='found-post-list'),

    path('create/lost', lost_post_create_view, name='create-lost-post'),
    path('create/found', found_post_create_view, name='create-found-post'),

    path('<int:id>/delete/', delete_post_view, name='post-delete')
]