# coding:utf-8
from __future__ import unicode_literals

from django.contrib import admin
from django.urls import re_path, path

from .custom_site import custom_site
from blog.views import (
    IndexView, CategoryView, TagView, PostView,
    AuthorView
)
from config.views import LinkView
from comment.views import CommentView

urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),
    re_path(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category'),
    re_path(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag'),
    re_path(r'^post/(?P<pk>\d+)/$', PostView.as_view(), name='detail'),
    re_path(r'^author/(?P<author_id>\d+)/$', AuthorView.as_view(), name='author'),
    re_path(r'^links/$', LinkView.as_view(), name='links'),
    re_path(r'^comment/$', CommentView.as_view(), name='comment'),

    path('admin/', admin.site.urls, name='admin'),
    path('cus_admin/', custom_site.urls, name='cus_admin'),

    # re_path(r'^search/$', SearchView.as_view(), name='search'),
]
