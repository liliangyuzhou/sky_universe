# coding=utf-8
# @Time    : 2020/8/11 11:41 上午
# @Author  : liliang
# @File    : base.py

from django.core import serializers
import json
class Base:
    """模型基类，供各个模型序列化数据格式"""
    def serializers_json(self,field=()):
        """
        序列化成json对象
        :param field:选择序列化的属性，通过制定fields参数，fields是一个元组参数，元素是选择要序列化的属性
        :return:
        """
        data_json=serializers.serialize('json',self,field=field)
        return data_json

    def serializers_dict(self,field):
        """
        序列化为字典
        :param field:
        :return:
        """
        data_json=self.serializers_json(field=field)
        data_dict=json.load(data_json)
        return data_dict