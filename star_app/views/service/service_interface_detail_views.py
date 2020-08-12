# coding=utf-8
# @Time    : 2020/8/5 2:39 下午
# @Author  : liliang
# @File    : interface_list_views.py
from django.views import View
from django.forms.models import model_to_dict

from star_app.models import interface
from star_app.common import reponse_fail, response_success
from star_app.my_exception import MyException
from star_app.models.services import Services

import json


# service下面的接口操作，查看该服务下的所有接口，为什么不写在接口的类视图中，因为get方法已经被使用，所以只能新建一个类视图
class ServiceInterfaceDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        """
        获取某个服务下的接口列表
        :param request:
        :param pk: 指的是service_id
        :param args:
        :param kwargs:
        :return:
        """
        interfaces = interface.Interface.objects.filter(service_id=pk)
        ret=[]
        for i in interfaces:
            ret.append(model_to_dict(i))
        return response_success(ret)
