# coding=utf-8
# @Time    : 2020/8/24 11:22 上午
# @Author  : liliang
# @File    : mock.py
from django.db import models
from star_app.models.object_field import ObjectField


class Mock(models.Model):
    name = models.CharField('name', blank=False, max_length=200)
    description = models.TextField('description', default='', max_length=500)

    method = models.CharField('method', blank=False, max_length=20, default="get")
    response = ObjectField('response', default={})

    def __str__(self):
        return self.name
