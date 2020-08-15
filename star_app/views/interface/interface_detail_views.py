# coding=utf-8
# @Time    : 2020/8/5 3:32 下午
# @Author  : liliang
# @File    : interface_detail_views.py

from django.views import View
from django.forms.models import model_to_dict
from django.contrib import auth

from star_app.models import interface
from star_app.forms import interface_form
from star_app.common import reponse_fail,response_success
from star_app.my_exception import MyException

import json


class InterfaceDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        """
        获取单个接口的数据
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            interfaces=interface.Interface.objects.get(id=pk)
            print(interfaces)
        except interface.Interface.DoesNotExist:
            return reponse_fail()
        else:
            return response_success(model_to_dict(interfaces))

    def delete(self, request,pk, *args, **kwargs):
        """
        删除单个接口
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            interface.Interface.objects.filter(id=pk).delete()
        except interface.Interface.DoesNotExist:
            return reponse_fail()
        else:
            return response_success()

    def put(self, request, pk, *args, **kwargs):
        """
        更新单个接口
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        params = json.loads(body)
        form = interface_form.InterfaceForm(params)
        result = form.is_valid()
        if result:
            interfaces = interface.Interface.objects.filter(id=pk).update(**form.cleaned_data)
            if interfaces:
                return response_success()
            else:
                raise MyException(message="更新接口失败！")
        else:
            # 表单验证不通过，打印出来错误信息
            print(form.errors.as_json())
            raise MyException(message="请输入正确的参数！")
