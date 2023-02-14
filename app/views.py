from django.shortcuts import render

from .models import *
from authentication.models import *

def homepage(request):
    first_two_posts = Post.objects.all().order_by("-date_created")[:2]

    context_for_homepage = {
        'all_posts' : first_two_posts,
    }

    return render(request, 'owren/index.html', context_for_homepage)

def post_article(request,id):
    
    get_post = Post.objects.filter(id=id)
    post_info = { 
        'post' : get_post
    }

    return render(request, 'owren/article.html', post_info)