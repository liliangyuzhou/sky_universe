
# coding=utf-8
# @Time    : 2020/8/3 7:52 下午
# @Author  : liliang
# @File    : middleware.py

from django.utils.deprecation import MiddlewareMixin
from django.db import DatabaseError
from star_app.common import reponse_fail
import traceback
from star_app.my_exception import MyException

class MyExceptionMiddleware(MiddlewareMixin):
    #只要出现异常，都会在这个函数中，可以捕捉所有的异常 raise MyException(message=")_
    #只有没有被捕获的的异常才会被全局捕获。意思就是自己手动try……except的。自己主动处理了，是不会被自己写在中间件的全部捕获的
    def process_exception(self,request,exception):

        #打印堆栈的异常
        print(traceback.format_exc())

        if isinstance(exception,MyException):
            print("我自定义的错误！")
            return reponse_fail(exception.message)
        elif isinstance(exception,DatabaseError):
            print("数据库错误！")
            return reponse_fail("数据库错误！")
        else:
            print("未知错误！")
            return reponse_fail("未知错误！")

    # def process_request(self,request):
    #     print("这是自定义中间件的请求")
    #
    # def process_response(self, request,response):
    #     print("这是自定义中间件的返回")
    #     return response

