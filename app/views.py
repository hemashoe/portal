from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.views.decorators.cache import cache_page

from api.models import News, Post, Profile
from .models import Interest

# from owren.settings import CACHE_TTL

# @cache_page(CACHE_TTL)
def homepage(request):
    navbar_items = Interest.objects.all()
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
        'navbar_items' : navbar_items,
        'two_posts' : two_popular_posts,
        'all_posts' : post_list, 
        'popular_articles' : popular_articles,
    }

    return render(request, 'owren/index.html', context_for_homepage)


# @cache_page(CACHE_TTL)
def post_detailed(request, slug_id):
    navbar_items = Interest.objects.all()
    post = get_object_or_404(Post, slug=slug_id)
    similar_posts = Post.objects.exclude(title=post.title).order_by('-date_created')[:3]
    from_author = Post.objects.filter(author = post.author).exclude(title=post.title).last()
    
    context_for_postdetailed = {
        'navbar_items' : navbar_items,
        "post" : post,
        "similar_posts" : similar_posts,
        "from_author" : from_author,
    }

    return render(request, 'owren/post_detailed.html', context_for_postdetailed)

# @cache_page(CACHE_TTL)
def news_detailed(request, slug_id):
    navbar_items = Interest.objects.all()
    news = get_object_or_404(News, slug=slug_id)
    similar_news = News.objects.exclude(title=news.title).order_by('-date_created')[:3]
    from_author = News.objects.filter(author = news.author).exclude(title=news.title).last()
    
    context_for_newsdetailed = { 
        'navbar_items' : navbar_items,
        "news" : news,
        "similar_news" : similar_news,
        "from_author" : from_author,
    }
    
    return render(request, 'owren/news_detailed.html', context_for_newsdetailed)

def profile_detailed(request, username):
    navbar_items = Interest.objects.all()
    user = get_object_or_404(Profile, user=username)
    posts_from_user = Post.objects.filter(author=user).order_by('-date_created')
    
    context_for_profiledetailed = {
        'navbar_items' : navbar_items,
        "user" : user,
        "posts_from_user" : posts_from_user,
    }

    return render(request, 'owren/profile_detailed.html', context_for_profiledetailed)

def category_detailed(requiest, slug_id):
    navbar_items = Interest.objects.all()
    category = Interest.objects.get(slug=slug_id)
    posts_from_category = Post.objects.filter(interests=category.id).order_by('-date_created')

    context_for_category_detailed = {
        'navbar_items' : navbar_items,
        "category" : category,
        "posts_from_category" : posts_from_category,
    }
    
    return render(requiest, 'owren/category.html', context_for_category_detailed)


def about(request):
    navbar_items = Interest.objects.all()

    context_for_about = {
        'navbar_items' : navbar_items,
    }

    return render(request, 'owren/about.html', context_for_about)