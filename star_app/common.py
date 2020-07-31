# coding=utf-8
# @Time    : 2020/7/27 7:23 下午
# @Author  : liliang
# @File    : common.py

import json
from django.http import JsonResponse,HttpResponse

def response_json(success,message,data):
    result={}
    result['success']=success
    result['message']=message
    result['data']=data
    return JsonResponse(result,safe=False)

def response_success(data={}):
    return response_json(True,"",data)


def reponse_fail(message):
    return response_json(False,message,"")