from django.urls import path

from .views import homepage

urlpatterns = [
    path('', homepage, name='main'),
    # path('post/<slug:post_slug>/', post_article, name='post_id'),
]
