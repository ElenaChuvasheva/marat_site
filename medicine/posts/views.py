from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render

from .forms import PostForm
from .models import Post
from .utils import paginate_posts

User = get_user_model()

# TODO разобраться с обрезанием отзыва, убрать в константу


def index(request):
    """Главная страница."""
    # page_obj = paginate_posts(request, Post.objects.filter(visible=True))
    page_obj = Post.objects.filter(visible=True)[:3]
    context = {
        "page_obj": page_obj,
    }
    return render(request, "posts/index.html", context)


def posts_list(request):
    page_obj = paginate_posts(request, Post.objects.filter(visible=True))
    context = {
        "page_obj": page_obj,
    }
    return render(request, "posts/posts_list.html", context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {"post": post}
    return render(request, "posts/post_detail.html", context)


def post_create(request):
    form = PostForm(
        request.POST or None,
        files=request.FILES or None,
    )

    if form.is_valid():
        form_data = form.save(commit=False)
        form_data.save()

        return render(request, "posts/post_sent.html")

    context = {
        "form": form,
    }
    return render(request, "posts/create_post.html", context)
