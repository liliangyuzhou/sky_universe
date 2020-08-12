# coding=utf-8
# @Time    : 2020/8/5 2:39 下午
# @Author  : liliang
# @File    : interface_list_views.py
from django.views import View
from star_app.models.services import Services,IS_ROOT
from star_app.forms import services_form
from star_app.common import reponse_fail,response_success
from star_app.my_exception import MyException
from star_app.utils.serviceutil import ServiceUtil

import json
class ServiceListView(View):
    def get(self,request,*args, **kwargs):
        """
        获取所有的服务列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        res=ServiceUtil.get_service_tree_structure(IS_ROOT)
        return response_success(res)

    def post(self,request,*args, **kwargs):
        """
        创建一个服务
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        params = json.loads(body)
        form = services_form.ServicesForm(params)
        result = form.is_valid()
        if result:
            service = Services.objects.create(name=form.cleaned_data.get("name"),
                                                       description=form.cleaned_data.get("description"),
                                                       parent=form.cleaned_data.get("parent"))
            if service:
                return response_success()
            else:
                raise MyException(message="添加服务失败！")

        else:
            # 表单验证不通过，打印出来错误信息
            print(form.errors.as_json())
            raise MyException(message="请输入正确的参数！")
