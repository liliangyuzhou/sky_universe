# coding=utf-8
# @Time    : 2020/8/5 3:32 下午
# @Author  : liliang
# @File    : interface_detail_views.py

from django.views import View
from django.forms.models import model_to_dict
from django.contrib import auth

from star_app.models import services
from star_app.forms import services_form
from star_app.common import reponse_fail,response_success
from star_app.my_exception import MyException

import json


class ServiceDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        """
        获取单个服务的数据
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            service=services.Services.objects.get(pk)
        except services.Services.DoesNotExist:
            return reponse_fail()
        else:
            return response_success(model_to_dict(service))

    def delete(self, request,pk, *args, **kwargs):
        """
        删除单个服务
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            services.Services.objects.filter(id=pk).delete()
        except services.Services.DoesNotExist:
            return reponse_fail()
        else:
            return response_success()

    def put(self, request, pk, *args, **kwargs):
        """
        更新单个服务
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        params = json.loads(body)
        form = services_form.ServicesForm(params)
        result = form.is_valid()
        if result:
            service = services.Services.objects.filter(id=pk).update(**form.cleaned_data)
            if service:
                return response_success()
            else:
                raise MyException(message="更新服务失败！")
        else:
            # 表单验证不通过，打印出来错误信息
            print(form.errors.as_json())
            raise MyException(message="请输入正确的参数！")
