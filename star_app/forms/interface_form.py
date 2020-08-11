# coding=utf-8
# @Time    : 2020/8/11 2:08 下午
# @Author  : liliang
# @File    : interface.py
from django.db import models
from django import forms
from star_app.models.services import Services
from star_app.forms.object_field import ObjectField


class InterfaceForm(forms.Form):
    name = forms.CharField(max_length=200, required=True)
    description = forms.CharField(max_length=200, required=False)
    host = forms.CharField(max_length=200, required=False)
    url = forms.CharField(max_length=500, required=True)
    method = forms.CharFiel(max_length=20, required=True)
    headers = ObjectField(required=False)
    parameter = ObjectField(required=False)
    parameter_type = forms.CharField(required=False, max_length=20)
    response = forms.TextField(required=False)
    response_type = forms.CharField(required=False, max_length=20)

    asserts = forms.TextField(required=False)
    service_id = forms.IntegerField(required=True)

    def clean_service_id(self):
        service_id = self.cleaned_data.get('service_id')
        try:
            Services.objects.get(pk=service_id)
        except Services.DoesNotExist:
            raise forms.ValidationError("服务不存在")
        else:
            return service_id
