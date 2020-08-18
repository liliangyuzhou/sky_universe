# coding=utf-8
# @Time    : 2020/8/5 2:39 下午
# @Author  : liliang
# @File    : debug_list_views.py
from django.views import View
from star_app.models.interface import Interface
from star_app.forms import interface_form
from star_app.common import reponse_fail,response_success
from star_app.my_exception import MyException
from django.forms import model_to_dict


import json
class InterfaceListView(View):
    def get(self,request,*args, **kwargs):
        """
        获取全部的接口列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        interfaces=Interface.objects.all()
        ret=[]
        for interface in interfaces:
            ret.append(model_to_dict(interface))
        return response_success(ret)

    def post(self,request,*args, **kwargs):
        """
        创建接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        params = json.loads(body)
        print(params)
        form = interface_form.InterfaceForm(params)
        # print(form)
        result = form.is_valid()
        print(form.cleaned_data)
        if result:
            service = Interface.objects.create(**form.cleaned_data)

            if service:
                return response_success()
            else:
                raise MyException(message="添加服务失败！")

        else:
            # 表单验证不通过，打印出来错误信息
            print(form.errors.as_json())
            raise MyException(message="请输入正确的参数！")
