# coding=utf-8
# @Time    : 2020/8/11 2:41 下午
# @Author  : liliang
# @File    : object_field.py

from django.db import models
import json
class ObjectField(models.TextField):
    """自定义一个字典类型的field"""
    description = "store python dict"

    def __init__(self, *args, **kwargs):
        super(models.TextField,self).__init__(*args, **kwargs)

    def from_db_value(self, value,expression,connection,context):
        """从数据库中读取，只处理两种情况，None和 不是None，不是的时候转换为json格式"""
        if value is None:
            return value
        try:
            ret=json.loads(value)
        except:
            return None
        else:
            return ret
    def to_python(self, value):
        """
        to_python通过反序列化和从表单使用的clean()方法调用，作为一般规则，to_python方法应该处理下面所有的参数
        字符串，None（如果字段null=True)
        :param value:
        :return:
        """
        if value is None:
            value=dict()
        if isinstance(value,dict):
            return value
        try:
            ret = json.loads(value)
        except:
            return None
        else:
            return ret

    def get_prep_value(self, value):
        """
        保存数据的时候会调用，把json格式的数据保存为dict
        :param value:
        :return:
        """
        if value is None:
            return value
        return json.dumps(value,ensure_ascii=False)