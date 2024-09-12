from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/<int:post_id>/", views.post_detail, name="post_detail"),
    path("create/", views.post_create, name="post_create"),
    path("opinions/", views.posts_list, name="posts_list"),
]
