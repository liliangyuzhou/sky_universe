# coding=utf-8
# @Time    : 2020/8/5 3:32 下午
# @Author  : liliang
# @File    : mock_detail_views.py

from django.views import View
from django.forms.models import model_to_dict
from django.http import JsonResponse
from star_app.models.mock import Mock
from star_app.forms.mock_form import MockForm
from star_app.common import reponse_fail, response_success
from star_app.my_exception import MyException
from star_app.models.task import Task, TaskInterface
from star_app.models.results import TaskResult, InterfaceResult
import json


class MockDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        """
        获取单个mock的数据
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            mock = Mock.objects.get(pk)
        except Mock.DoesNotExist:
            return reponse_fail()
        else:
            return response_success(model_to_dict(mock))

    def delete(self, request, pk, *args, **kwargs):
        """
        删除单个mock任务
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            Mock.objects.filter(id=pk).delete()
        except Mock.DoesNotExist:
            return reponse_fail()
        else:
            return response_success()

    def put(self, request, pk, *args, **kwargs):
        """
        更新单个mock任务
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        params = json.loads(body)
        form = MockForm(params)
        result = form.is_valid()
        if result:
            mock = Mock.objects.filter(id=pk).update(**form.cleaned_data)
            if mock:
                return response_success()
            else:
                raise MyException(message="更新MOCK任务失败！")
        else:
            # 表单验证不通过，打印出来错误信息
            print(form.errors.as_json())
            raise MyException(message="请输入正确的参数！")


"""调用创建的mock接口"""


# mock本质是定义一个响应，通过自定义的url，得到我们自定义的响应
def run_mock(request, pk):
    if not pk:
        raise MyException()
    mock = Mock.objects.get(id=pk)
    print(mock.method)
    print(request.method)
    if request.method == mock.method.upper():
        return JsonResponse(mock.response, safe=False)
    else:
        raise MyException(message="mock接口不存在！")
