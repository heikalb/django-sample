from django.urls import path

from .views import (
    post_detail_view,
    post_create_view,
    delete_post_view,
    post_list_view
)

urlpatterns = [
    path('create/', post_create_view, name='create-post'),
    path('<int:id>', post_detail_view, name='post-detail'),
    path('<int:id>/delete/', delete_post_view, name='post-delete'),
    path('post-list/', post_list_view, name='post-list')
]