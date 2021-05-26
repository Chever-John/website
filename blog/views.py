# Create your views here.
from django.shortcuts import render

from .models import Post, Category


def post_list(request, category_id=None, tag_id=None):
    """tag = None
    category = None
    if tag_id:
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            post_list_view = []
        else:
            post_list_view = tag.post_set.filter(status=Post.STATUS_NORMAL)
    else:
        post_list_view = Post.objects.filter(status=Post.STATUS_NORMAL)
        if category_id:
            try:
                category = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                category = None
            else:
                post_list_view = post_list.filter(category_id=category_id)
    context = {
        'category': category,
        'tag': tag,
        'post_list': post_list_view,
    }
    return render(request, 'blog/list.html', context=context)"""
    tag = None
    category = None

    if tag_id:
        post_list_view, tag = Post.get_by_tag(tag_id)
    elif category_id:
        post_list_view, category = Post.get_by_category(category_id)
    else:
        post_list_view = Post.latest_posts()

    context = {
        'category': category,
        'tag': tag,
        'post_list': post_list_view,
    }
    context.update(Category.get_navs())
    return render(request, 'blog/list.html', context=context)


def post_detail(request, post_id=None):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None

    context = {
        'post': post,
    }
    context.update(Category.get_navs())
    return render(request, 'blog/detail.html', context=context)
