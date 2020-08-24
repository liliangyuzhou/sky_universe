# coding=utf-8
# @Time    : 2020/8/5 2:39 下午
# @Author  : liliang
# @File    : mock_list_views.py
from django.views import View
from star_app.forms import mock_form
from star_app.common import response_success
from star_app.my_exception import MyException
from star_app.models.mock import Mock
from star_app.models.results import TaskResult, InterfaceResult
from django.forms import model_to_dict

import json


class MockListView(View):
    def get(self, request, *args, **kwargs):
        """
        获取所有的mock列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        mocks = Mock.objects.all()
        ret = []
        for i in mocks:
            ret.append(model_to_dict(i))
        return response_success(ret)

    def post(self, request, *args, **kwargs):
        """
        创建一个mock
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        params = json.loads(body)
        form = mock_form.MockForm(params)
        result = form.is_valid()
        if result:
            mock = Mock.objects.create(**form.cleaned_data)
            if mock:
                return response_success()
            else:
                raise MyException(message="添加mock接口失败！")

        else:
            # 表单验证不通过，打印出来错误信息
            print(form.errors.as_json())
            raise MyException(message="请输入正确的参数！")
