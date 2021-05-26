from django.urls import path, re_path
from django.contrib import admin

from blog.views import (
    IndexView, CategoryView, TagView,
    PostDetailView,
)
from config.views import links
from .custom_site import custom_site

urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),
    re_path(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),
    re_path(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
    re_path(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post-detail'),
    # re_path(r'^links/$', links),
    # re_path(r'^super_admin/', admin.site.urls),
    # re_path(r'^/admin/', custom_site.urls),

    path('links/', links, name='links'),
    path('super_admin/', admin.site.urls, name='super-admin'),
    path('admin/', custom_site.urls, name='admin'),
]
