from django.urls import path

from .views import *

urlpatterns = [
    path('', homepage, name='main'),
    path('post/<int:id>/', post_article, name='post_id'),
]
