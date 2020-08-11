# coding=utf-8
# @Time    : 2020/8/11 2:08 下午
# @Author  : liliang
# @File    : interface.py
from django.db import models
from star_app.models.services import Services
from star_app.models.base import Base
from star_app.models.object_field import ObjectField


class Interface(models.Model, Base):

    name = models.CharField('name', blank=False, max_length=200)
    description = models.CharField('description', default='',max_length=500)
    host = models.CharField('host', default="", max_length=200)
    url = models.CharField('url', blank=False, max_length=500)
    method = models.CharField('method', blank=False, max_length=20)
    headers = ObjectField('headers', default={})
    parameter = ObjectField('parameter', default={})
    parameter_type = models.CharField('parameter_type,json or form', default="json", max_length=20)
    response = models.TextField('response', default='')
    response_type = models.CharField('parameter_type,json or form', default="json", max_length=20)

    asserts = models.TextField('asserts', default='')
    service = models.ForeignKey(Services, blank=False, related_name="services_interface", on_delete=models.SET_NULL,
                                null=True)
