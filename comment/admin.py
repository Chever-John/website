# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from website.base_admin import BaseOwnerAdmin
from website.custom_site import custom_site
from .models import Comment


# Register your models here.

@admin.register(Comment, site=custom_site)
class CommentAdmin(BaseOwnerAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')
