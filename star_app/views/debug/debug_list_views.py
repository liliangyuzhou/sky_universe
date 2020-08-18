# coding=utf-8
# @Time    : 2020/8/5 2:39 下午
# @Author  : liliang
# @File    : debug_list_views.py
from django.views import View
from star_app.common import response_success
from star_app.my_exception import MyException
from star_app.forms.debug_form import DebugForm
from star_app.utils.request_util import Request_Utils
import logging

logger = logging.getLogger(__name__)  # 这里用__name__通用,自动检测.


import json
class DebugListView(View):


    def post(self,request,*args, **kwargs):
        """
        调试接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        print(body)
        params = json.loads(body)
        # print(params)
        form = DebugForm(params)
        # print(form)
        result = form.is_valid()
        print(form.cleaned_data)
        if result:
            # method=form.cleaned_data['method']
            # url=form.cleaned_data['url']
            # headers = form.cleaned_data['headers']
            # parameter = form.cleaned_data['parameter']
            # parameter_type = form.cleaned_data['parameter_type']
            # res=Request_Utils.row_request(method,url, headers, parameter, parameter_type)

            res = Request_Utils.row_request(**form.cleaned_data)



            if res:
                return response_success(res)
            else:
                raise MyException(message="调用接口失败！")

        else:
            # 表单验证不通过，打印出来错误信息
            print(form.errors.as_json())
            raise MyException(message="请输入正确的参数！")
