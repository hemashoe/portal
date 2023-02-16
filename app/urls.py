from django.urls import path

from .views import homepage, post_detailed, news_detailed, about

urlpatterns = [
    path('', homepage, name='main'),
    path('posts/<slug:slug_id>/', post_detailed, name='post_detailed'),
    path('news/<slug:slug_id>/', news_detailed, name='news_detailed'),
    path('about_us', about, name='about')
]
