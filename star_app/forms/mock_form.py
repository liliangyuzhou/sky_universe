# coding=utf-8
# @Time    : 2020/8/24 11:22 上午
# @Author  : liliang
# @File    : mock_form.py

from django import forms
from star_app.forms.object_field import ObjectField


class MockForm(forms.Form):
    name = forms.CharField(max_length=200, required=True)
    description = forms.CharField(max_length=200, required=False)

    method = forms.CharField(max_length=20, required=True)
    response = ObjectField(required=False)
