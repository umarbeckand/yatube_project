from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from .models import Post, Group

User = get_user_model()  # ← добавлено!

def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)

def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=author).order_by('-pub_date')
    context = {
        'author': author,
        'posts': posts,
        'posts_count': posts.count()
    }
    return render(request, 'posts/profile.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    author_posts_count = Post.objects.filter(author=post.author).count()
    context = {
        'post': post,
        'author_posts_count': author_posts_count
    }
    return render(request, 'posts/post_detail.html', context)
