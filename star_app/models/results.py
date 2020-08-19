# coding=utf-8
# @Time    : 2020/8/18 4:35 下午
# @Author  : liliang
# @File    : results.py

from django.db import models
from star_app.models.base import Base
from star_app.models.object_field import ObjectField
from star_app.models.interface import Interface
from star_app.models.task import Task


class TaskResult(models.Model, Base):
    version = models.CharField("version", default=1,max_length=10000)
    create_time = models.DateTimeField("创建时间", auto_created=True, )
    update_time = models.DateTimeField(auto_now=True)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)

    # interface_results = models.ManyToManyField(InterfaceResult)

    def __str__(self):
        return self.version


class InterfaceResult(models.Model, Base):
    """单个接口请求的一次历史结果"""
    interface = models.ForeignKey(Interface, on_delete=models.SET_NULL, null=True)
    task_result = models.ForeignKey(TaskResult, on_delete=models.SET_NULL, null=True)

    name = models.CharField('name', blank=False, max_length=200)
    description = models.TextField('description', default='', max_length=500)
    host = models.CharField('host', default="", max_length=200)
    url = models.CharField('url', blank=False, max_length=500)
    method = models.CharField('method', blank=False, max_length=20)
    headers = ObjectField('headers', default={})
    parameter = ObjectField('parameter', default={})
    parameter_type = models.CharField('parameter_type,json or form', default="json", max_length=20)
    response = ObjectField('response', default='')
    response_type = models.CharField('parameter_type,json or form', default="json", max_length=20)

    asserts = ObjectField('asserts', default=[])
    create_time = models.DateTimeField("创建时间", auto_created=True, )
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
