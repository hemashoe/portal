"""Owren URL Configuration"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # path('', include('app.urls')),
]

if settings.DEBUG: 
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns 
    urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root =settings.STATIC_ROOT)
