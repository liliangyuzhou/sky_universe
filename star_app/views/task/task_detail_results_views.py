# coding=utf-8
# @Time    : 2020/8/5 3:32 下午
# @Author  : liliang

from django.views import View
from django.forms.models import model_to_dict
import datetime
from star_app.common import response_success
from star_app.my_exception import MyException
from star_app.models.task import Task, TaskInterface
from star_app.models.interface import Interface
from star_app.utils.task_utils import TaskUtils
from star_app.models.results import TaskResult,InterfaceResult
import json

"""task任务下接口结果的查询接口"""


class TaskDetailVsersionView(View):
    def get(self, request, pk, *args, **kwargs):
        """
        获取单个任务下的版本列表
        """
        results=TaskResult.objects.filter(task_id=pk).order_by("-version")
        ret=[]
        for i in results:
            tem=dict()
            tem["version"]=i.version
            tem["task_id"]=i.id
            tem["create_time"]=i.create_time.strftime("%Y-%m-%d %H:%M:%S")
            ret.append(tem)
        return response_success(ret)


class TaskDetailVersionResultsView(View):
    def get(self, request, pk, *args, **kwargs):
        """
        获取单个版本结果列表
        """
        results=InterfaceResult.objects.filter(task_result_id=pk).order_by("-version")
        ret=[model_to_dict(i) for i in results]
        return response_success(ret)
