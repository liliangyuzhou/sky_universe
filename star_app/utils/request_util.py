# coding=utf-8
# @Time    : 2020/8/17 10:07 上午
# @Author  : liliang
# @File    : request_util.py

import requests
import json
import traceback

import logging

logger = logging.getLogger(__name__)  # 这里用__name__通用,自动检测.
class Request_Utils:

    @classmethod
    def form_revrese_json(cls, parameter):
        """
        将form表单格式的入参转化为字典的形式
        :param parameter:
        :return:
        """
        ret = {}
        if not parameter:
            return ret
        for i in parameter:
            try:
                i_type = i.get("type", None)
                if i_type is None:
                    continue
                key = i.get("key", None)
                if key is None:
                    continue
                value = i.get("value", None)
                if value is None:
                    continue
                if i.type == "string":
                    ret["key"] = str(value)
                elif i.type == "int":
                    ret["key"] = int(value)
                elif i.type == "float":
                    ret["key"] = float(value)
                elif i.type == "boolean":
                    ret["key"] = bool(value)
                else:
                    continue
            except:
                continue
            return ret

    @classmethod
    def __get(cls, url, data, headers):
        response = requests.get(url=url, params=data, headers=headers)
        return response.text

    @classmethod
    def __set_header(cls, headers, parameter_type):
        if parameter_type == "json":
            headers["content-type"] = "application/json"
        elif parameter_type == "form":
            headers["content-type"] = "application/x-www-form-urlencoded"
        return headers

    @classmethod
    def __post(cls, url, headers, parameter, parameter_type):
        headers=cls.__set_header(headers, parameter_type)
        response = requests.post(url=url, data=parameter, headers=headers, )
        return response.text

    @classmethod
    def __put(cls, url, parameter, headers, parameter_type):
        headers = cls.__set_header(headers, parameter_type)
        response = requests.put(url=url, data=parameter, headers=headers)
        return response.text

    @classmethod
    def __delete(cls, url, headers, parameter, parameter_type):
        headers = cls.__set_header(headers, parameter_type)
        response = requests.delete(url=url, headers=headers, data=parameter)
        return response.text

    @classmethod
    def row_request(self, method, url, headers, parameter, parameter_type):
        if parameter_type == "form":
            parameter = self.form_revrese_json(parameter)
        try:
            if method.upper() == "GET":
                return self.__get(url, headers, parameter)
            elif method.upper() == "POST":
                return self.__post(url, headers, parameter, parameter_type)
            elif method.upper() == "PUT":
                return self.__put(url, headers, parameter, parameter_type)
            elif method.upper() == "DELETE":
                return self.__delete(url, headers, parameter, parameter_type)
        except Exception:
            return traceback.format_exc()
