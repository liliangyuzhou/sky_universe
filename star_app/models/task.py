# coding=utf-8
# @Time    : 2020/8/11 2:08 下午
# @Author  : liliang
# @File    : interface.py
from django.db import models
from star_app.models.base import Base
from star_app.models.interface import Interface

TASK_STATUS = ((0, "未执行"), (1, "执行中"), (2, "执行完成"))


class Task(models.Model, Base):
    """任务表"""
    name = models.CharField('name', blank=False, max_length=200)
    description = models.TextField('description', default='', max_length=500)
    status = models.IntegerField("状态", choices=TASK_STATUS, default=0)

    # interfaces = models.ManyToManyField(Interface)  # 等于直接创建了TaskInterface这张表，不用再次定义下面这张表，考虑到任务中一个接口可以多次选择，所以不使用django原生的多对多生成方式

    def __str__(self):
        return self.name




class TaskInterface(models.Model, Base):
    """因为任务和接口是多对多，所有2张表中间要建一张关联表，设计为2个一对多的关系"""
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    interface = models.ForeignKey(Interface, on_delete=models.SET_NULL, null=True)
