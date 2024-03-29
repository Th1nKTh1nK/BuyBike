from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Ad


def post_list(request):
    posts = Ad.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
