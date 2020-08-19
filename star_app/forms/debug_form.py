# coding=utf-8
# @Time    : 2020/8/11 2:08 下午
# @Author  : liliang
# @File    : debug_form.py

from django import forms
from star_app.forms.object_field import ObjectField


class DebugForm(forms.Form):
    url = forms.CharField(max_length=500, required=True)
    method = forms.CharField(max_length=20, required=True)
    headers = ObjectField(required=False)
    parameter = ObjectField(required=False)
    parameter_type = forms.CharField(required=False, max_length=20)
