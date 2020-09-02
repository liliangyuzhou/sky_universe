# coding=utf-8
# @Time    : 2020/8/5 3:32 下午
# @Author  : liliang

from django.views import View
from django.forms.models import model_to_dict

from star_app.common import response_success
from star_app.my_exception import MyException
from star_app.models.task import Task, TaskInterface
from star_app.models.interface import Interface
from star_app.utils.task_utils import TaskUtils
import json

"""task任务下接口的增删改查"""


class TaskDetailInterfacesView(View):
    def get(self, request, pk, *args, **kwargs):
        """
        获取单个任务下的所有接口数据
        :param request:
        :param pk:任务的id
        :param args:
        :param kwargs:
        :return:
        """

        interfaces = TaskInterface.objects.filter(task_id=pk)
        last_result = TaskUtils.get_last_results(task_id=pk)
        # # 列表表达式
        # ret = [model_to_dict(i.interface) for i in interfaces]
        # # print(ret)
        # return response_success(ret)
        ret = []
        for i in interfaces:
            tem = model_to_dict(i.interface)
            tem["task_interface_id"] = i.id
            r="无"
            if last_result is not None:
                r=TaskUtils.get_last_interface_result(last_result.id, i.interface_id)
            tem["result"] = r
            ret.append(tem)
        return response_success(ret)

    def post(self, request, pk, *args, **kwargs):
        """
        增加单个任务下的接口:其实增加一个任务下的接口，就是向TaskInterface表增加一条数据
        数据结构：
        {
        interfaces:[1,2,3,4,5,]
        }
        :param request:
        :param pk:任务的id
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        params = json.loads(body)
        interfaces = params.get("interfaces", [])
        if not isinstance(interfaces, list):
            raise MyException(message="数据格式不正确！")
        try:
            task = Task.objects.get(id=pk)
        except Task.DoesNotExist:
            raise MyException(message="任务不存在！")
        for i in interfaces:
            try:
                Interface.objects.get(id=i)
            except Interface.DoesNotExist:
                raise MyException(message="接口不存在，请检查数据！")
            TaskInterface.objects.create(task_id=task.id, interface_id=i)
        return response_success()

    # def delete(self, request, pk, *args, **kwargs):
    #     """
    #     删除单个任务下的接口
    #     :param request:
    #     :param pk:taskinterface的id
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #     TaskInterface.objects.filter(id=pk).delete()
    #     return response_success()

    def delete(self, request, pk, *args, **kwargs):
        """
        删除单个任务下的接口
        {
        task_interface_id:1
        }
        :param request:
        :param pk:这里这样设计taskinterface的id，从外面传进来一个id
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        params = json.loads(body)
        task_interface_id = params.get("task_interface_id", None)
        if task_interface_id is None:
            raise MyException(message="接口不存在，请检查数据！")
        TaskInterface.objects.filter(id=task_interface_id).delete()
        return response_success()
