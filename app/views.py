from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from authentication.models import Post, News


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


def post_detailed(request, slug_id):
    post = get_object_or_404(Post, slug=slug_id)

    context_for_postdetailed = {
        "post" : post
    }

    return render(request, 'owren/post_detailed.html', context_for_postdetailed)

def news_detailed(request, slug_id):
    news = get_object_or_404(News, slug=slug_id)
    
    context_for_newsdetailed = { 
        "news" : news
    }
    
    return render(request, 'owren/news_detailed.html', context_for_newsdetailed)


def about(request):
    return render(request, 'owren/about.html')