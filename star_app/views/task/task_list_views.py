# coding=utf-8
# @Time    : 2020/8/5 2:39 下午
# @Author  : liliang
# @File    : interface_list_views.py
from django.views import View
from django.forms import model_to_dict
from star_app.forms import task_form
from star_app.common import response_success
from star_app.my_exception import MyException
from star_app.models.task import Task, TaskInterface
from star_app.models.results import TaskResult, InterfaceResult
from star_app.utils.task_utils import TaskUtils


import json


class TaskListView(View):
    def get(self, request, *args, **kwargs):
        """
        获取所有的task列表
        values可以指定查询出的数据要返回那些字段作为字典的字段
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        tasks = Task.objects.all()
        ret = []
        for i in tasks:
            task = dict()
            task["id"] = i.id
            task["name"] = i.name
            task["description"] = i.description
            task["status"] = i.get_status_display()  # 获取该字段choice的描述
            task["interface_count"] = TaskInterface.objects.filter(task_id=i.id).count()
            task["result_count"] = TaskResult.objects.filter(task_id=i.id).count()

            task["last_result"]=TaskUtils.get_last_results_summary(i.id)
            ret.append(task)
        return response_success(ret)

    def post(self, request, *args, **kwargs):
        """
        创建一个任务
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        params = json.loads(body)
        form = task_form.TaskForm(params)
        result = form.is_valid()
        if result:
            task = Task.objects.create(name=form.cleaned_data.get("name"),
                                       description=form.cleaned_data.get("description"),
                                       )
            if task:
                return response_success()
            else:
                raise MyException(message="添加服务失败！")

        else:
            # 表单验证不通过，打印出来错误信息
            print(form.errors.as_json())
            raise MyException(message="请输入正确的参数！")
