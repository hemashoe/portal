from django.urls import path

from .views import (about, homepage, news_detailed, post_detailed,
                    profile_detailed, category_detailed)

# urlpatterns = [
    # path('', homepage, name='main'),
    # path('posts/<slug:slug_id>/', post_detailed, name='post_detailed'),
    # path('news/<slug:slug_id>/', news_detailed, name='news_detailed'),
    # path('profile_info/<str:username>/', profile_detailed, name='profile_detailed'),
    # path('category/<slug:slug_id>', category_detailed, name='category_detailed'),
    # path('about_us/', about, name='about')
# ]
