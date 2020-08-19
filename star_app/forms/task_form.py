# coding=utf-8
# @Time    : 2020/8/11 2:08 下午
# @Author  : liliang
# @File    : interface.py

from django import forms

class TaskForm(forms.Form):
    name = forms.CharField(max_length=200, min_length=1, required=True,)
    description = forms.CharField(max_length=200, min_length=1, required=False,)
