from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.decorators.cache import cache_page

from datetime import datetime, timedelta

from authentication.models import News, Post, Profile, User

# from owren.settings import CACHE_TTL

# @cache_page(CACHE_TTL)
def homepage(request):
    two_popular_posts = Post.objects.filter(published=True).order_by("-date_created")[:2]
    all_posts = Post.objects.filter(published=True).order_by("-date_created")[2:]
    popular_articles = News.objects.filter(published=True).order_by("-date_created")[:10]
    paginator = Paginator(all_posts, 10)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:

        # If page is not an integer deliver the first page
        post_list = paginator.page(1)

    except EmptyPage:

        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)

    context_for_homepage = {
        'two_posts' : two_popular_posts,
        'all_posts' : post_list, 
        'popular_articles' : popular_articles,
    }

    return render(request, 'owren/index.html', context_for_homepage)


# @cache_page(CACHE_TTL)
def post_detailed(request, slug_id):
    post = get_object_or_404(Post, slug=slug_id)
    authour_info = Profile.objects.get(user=post.author)
    similar_posts = Post.objects.exclude(title=post.title).order_by('-date_created')[:3]
    from_author = Post.objects.filter(author = post.author).exclude(title=post.title).last()
    
    context_for_postdetailed = {
        "post" : post,
        'author' : authour_info,
        "similar_posts" : similar_posts,
        "from_author" : from_author,
    }

    return render(request, 'owren/post_detailed.html', context_for_postdetailed)

def profile_detailed(request, username):
    user = get_object_or_404(Profile, user=username)
    
    context_for_profiledetailed = {
        "user" : user,
    }

    return render(request, 'owren/profile_detailed.html', context_for_profiledetailed)


# @cache_page(CACHE_TTL)
def news_detailed(request, slug_id):
    news = get_object_or_404(News, slug=slug_id)
    author_info = User.objects.get(username=news.author)
    
    context_for_newsdetailed = { 
        "news" : news,
        "author" : author_info, 
    }
    
    return render(request, 'owren/news_detailed.html', context_for_newsdetailed)


def about(request):
    return render(request, 'owren/about.html')