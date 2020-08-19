# coding=utf-8
# @Time    : 2020/8/5 3:32 下午
# @Author  : liliang
# @File    : interface_detail_views.py

from django.views import View
from django.forms.models import model_to_dict
from star_app.models.task import Task
from star_app.forms.task_form import TaskForm
from star_app.common import reponse_fail, response_success
from star_app.my_exception import MyException
from star_app.models.task import Task, TaskInterface
from star_app.models.results import TaskResult, InterfaceResult
import json


class TaskDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        """
        获取单个任务的数据
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            task = Task.objects.get(pk)
            ret = dict()
            task["id"] = task.id
            task["name"] = task.name
            task["description"] = task.description
            task["status"] = task.get_status_display()  # 获取该字段choice的描述
            task["interface_count"] = TaskInterface.objects.filter(task_id=task.id).count()
            task["result_count"] = TaskResult.objects.filter(task_id=task.id).count()
        except Task.DoesNotExist:
            return reponse_fail()
        else:
            return response_success(ret)

    def delete(self, request, pk, *args, **kwargs):
        """
        删除单个任务
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            Task.objects.filter(id=pk).delete()
        except Task.DoesNotExist:
            return reponse_fail()
        else:
            return response_success()

    def put(self, request, pk, *args, **kwargs):
        """
        更新单个任务
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        params = json.loads(body)
        form = TaskForm(params)
        result = form.is_valid()
        if result:
            task = Task.objects.filter(id=pk).update(**form.cleaned_data)
            if task:
                return response_success()
            else:
                raise MyException(message="更新任务失败！")
        else:
            # 表单验证不通过，打印出来错误信息
            print(form.errors.as_json())
            raise MyException(message="请输入正确的参数！")
