# coding=utf-8
# @Time    : 2020/8/11 2:41 下午
# @Author  : liliang
# @File    : object_field.py

from django import forms
import json


class ObjectField(forms.Field):
    """自定义一个字典类型的form field"""
    description = "store python dict"

    def __init__(self, *args, **kwargs):
        super(ObjectField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        """
        to_python通过反序列化和从表单使用的clean()方法调用，作为一般规则，to_python方法应该处理下面所有的参数
        字符串，None（如果字段null=True)
        :param value:
        :return:
        """
        if value is None:
            return value
        try:
            ret = json.loads(value)
        except:
            return None
        else:
            return ret

    def validate(self, value):
        """
      验证参数是否正确
        :param value:
        :return:
        """
        if not isinstance(value, dict) or not isinstance(value, list):
            raise forms.ValidationError("格式不正确")
