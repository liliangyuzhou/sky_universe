# coding=utf-8
# @Time    : 2020/8/5 10:21 上午
# @Author  : liliang
# @File    : services_form.py
from django import forms


class ServicesForm(forms.Form):
    name = forms.CharField(max_length=200, min_length=1, required=True,)
    description = forms.CharField(max_length=200, min_length=1, required=False,)
    parent = forms.IntegerField(required=True)
