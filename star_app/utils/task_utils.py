# coding=utf-8
# @Time    : 2020/8/26 10:57 上午
# @Author  : liliang
# @File    : task_utils.py

from star_app.models.results import TaskResult, InterfaceResult


class TaskUtils:
    @classmethod
    def get_last_results(cls, task_id):
        """
        根据任务id获取该任务的最后一个结果版本
        """
        if not task_id:
            return None
        results = TaskResult.objects.filter(id=task_id).order_by("-version")
        if len(results) == 0:
            return None
        return results[0]

    @classmethod
    def get_result_summary(cls, result_id):
        """
        根据task_result_id，获取结果集的接口成功数，接口失败数，接口总数
        """
        ret = {
            "success": 0,
            "failed": 0,
            "total": 0
        }
        if not result_id:
            return ret
        result = InterfaceResult.objects.filter(task_result_id=result_id)

        for i in result:
            if i.success:
                ret["success"] += 1
            else:
                ret["failed"] += 1

        ret["total"] = ret["success"] + ret["failed"]
        return ret

    @classmethod
    def get_last_results_summary(cls, task_id):
        """
        获取一个任务的最后一次结果集的接口成功数，接口失败数，接口总数
        """
        if not task_id:
            return cls.get_result_summary(None)
        result = cls.get_last_results(task_id)
        if result is None:
            return cls.get_result_summary(None)
        ret = cls.get_result_summary(result.id)
        return ret

    @classmethod
    def get_last_interface_result(cls, result_id, interface_id):
        if not interface_id or not result_id:
            return "无"
        version = InterfaceResult.objects.filter(task_result_id=result_id, interface_id=interface_id)
        if len(version) == 0:
            return "无"
        if version[0].success:
            return "成功"
        else:
            return "失败"
