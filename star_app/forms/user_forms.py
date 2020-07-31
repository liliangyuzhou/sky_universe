# coding=utf-8
# @Time    : 2020/7/31 2:30 下午
# @Author  : liliang
# @File    : user_forms.py

from django import forms

#form就是一个对字典的校验
class UserForms(forms.Form):
    username=forms.CharField(max_length=20,min_length=3,required=True,
                             error_messages={"max_length":"最大可以传20个字符",
                                             "min_length":"最小可以传3个字符",
                                             "required":"用户名为必填字段"})
    password=forms.CharField(max_length=20,min_length=3,required=True,
                             error_messages={"max_length":"最大可以传20个字符",
                                             "min_length":"最小可以传3个字符",
                                             "required":"用户密码为必填字段"})