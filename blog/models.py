# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import markdown
from django.contrib.auth.models import User
from django.db import models
from django.db.models import F


class Post(models.Model):
    STATUS_ITEMS = (
        (1, '发布'),
        (2, '草稿'),
        (3, '删除'),
    )

    title = models.CharField(max_length=255, verbose_name="标题")
    desc = models.CharField(max_length=1024, blank=True, verbose_name="摘要")
    category = models.ForeignKey('Category', verbose_name="分类", on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField('Tag', related_name="posts", verbose_name="标签")

    content = models.TextField(verbose_name="正文", help_text="正文必须为MarkDown格式")
    html = models.TextField(verbose_name="渲染后的内容", default='', help_text="注：目前仅支持Markdown格式数据")
    is_markdown = models.BooleanField(verbose_name="使用markdown格式", default=True)
    status = models.IntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    pv = models.PositiveIntegerField(default=1, verbose_name="pv")
    uv = models.PositiveIntegerField(default=1, verbose_name="uv")

    def status_show(self):
        return '当前状态:%s' % self.status

    status_show.short_description = '展示状态'

    def increase_pv(self):
        return type(self).objects.filter(id=self.id).update(pv=F('pv') + 1)

    def increase_uv(self):
        return type(self).objects.filter(id=self.id).update(uv=F('uv') + 1)

    def save(self, *args, **kwargs):
        if self.is_markdown:
            config = {
                'codehilite': {
                    'use_pygments': False,
                    'css_class': 'prettyprint linenums',
                }
            }
            self.html = markdown.markdown(self.content, extensions=["codehilite"], extension_configs=config)

        return super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = "文章"
        ordering = ['-id']


class TestManager(models.Manager):
    def get_queryset(self):
        return super(TestManager, self).get_queryset().filter(status=1)


class Category(models.Model):
    objects = TestManager()

    STATUS_ITEMS = (
        (1, '可用'),
        (2, '删除'),
    )

    name = models.CharField(max_length=50, verbose_name="名称")
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
    is_nav = models.BooleanField(default=False, verbose_name="是否为导航")
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '分类'


class Tag(models.Model):
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除'),
    )

    name = models.CharField(max_length=10, verbose_name="名称")
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '标签'
        ordering = ['-id']
