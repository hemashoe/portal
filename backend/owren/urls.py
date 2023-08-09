from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    re_path(r"^ckeditor/", include("ckeditor_uploader.urls")),
    path("admin/", admin.site.urls),
]
