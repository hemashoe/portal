from django.shortcuts import render
from django.views import generic

from authentication.models import Post


def homepage(request):
    two_popular_posts = Post.objects.filter(published=True).order_by("-date_created")[:2]
    all_posts = Post.objects.filter(published=True).order_by("-date_created")[2:]
    context_for_homepage = {
        'two_posts' : two_popular_posts,
        'all_posts' : all_posts
    }

    return render(request, 'owren/index.html', context_for_homepage)


