# coding=utf-8
# @Time    : 2020/8/3 8:08 下午
# @Author  : liliang
# @File    : my_exception.py

class MyException(Exception):
    def __init__(self,message="参数错误"):
        self.message=message

    def __str__(self):
        return self.message