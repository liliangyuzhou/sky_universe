import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.views.generic import View

from star_app.common import response_json, reponse_fail, response_success
from star_app.forms import user_forms
from star_app.my_exception import MyException

# Create your views here.

import logging

logger = logging.getLogger(__name__)  # 这里用__name__通用,自动检测.


# 使用类的方式定义接口：根据restful风格，同一个url，根据不同的http方法区别不同的接口。eg：这里自己约定 注册：post，登陆：put，获取用户：get
# 好处是不用写很多url，后期维护方便。另外就是不需要根据方法判断if request.method == "POST" else: return HttpResponse(404)，
# 来判断方法是否正确，类试图的写法自动会判断是不是正确的请求方式，不正确页面返回404页面
class UserViews(View):

    def get(self, request, *args, **kwargs):
        # 通过login(request,user)设置了session，可以通过request.user获取用户
        # raise MyException("登陆失败了！")
        token = request.META.get("HTTP_TOKEN", None)
        logger.info('aaa')
        print(token)
        if token is None:
            raise MyException(message="用户未登录")
            # return reponse_fail(message="用户未登录")
        else:
            try:
                # 根据head中的token获取session对象
                session = Session.objects.get(pk=token)

            except Session.DoesNotExist:
                raise MyException(message="session失效")
                # return reponse_fail(message="session失效")
            except Exception as e:
                print(e)
                raise MyException(message="未知错误")
                # return reponse_fail(message="未知错误")
            else:
                # 固定写法，Django本身session获取user_id
                user_id = session.get_decoded().get('_auth_user_id', None)
                if user_id is None:
                    raise MyException(message="用户ID失效！")
                    # return reponse_fail(message="用户ID失效！")
                try:
                    user = User.objects.filter(pk=user_id).first()
                    print(user.username)
                except User.DoesNotExist:
                    raise MyException(message="用户不存在！")
                    # return reponse_fail(message="用户不存在")
                return response_success(data={'username': user.username, 'id': user.id})

    def post(self, request, *args, **kwargs):
        body = request.body
        params = json.loads(body)
        print(params)
        form = user_forms.UserForms(params)
        result = form.is_valid()
        print(result)
        if result:
            # user=User.objects.create_user(username=str(params['username']),password=str(params['password']))
            # 可以使用form.cleaned_data来获取对应的值，cleaned_data可以；理解为一个校验过的字典，和params一样的值
            user = User.objects.create_user(username=form.cleaned_data.get("username"),
                                            password=form.cleaned_data.get("password"))
            if user:
                auth.login(request, user)
                # 获取设置的session值
                session = request.session.session_key
                return response_success()
            else:
                raise MyException(message="添加用户失败！")
                # return reponse_fail(message="添加用户失败！")
        else:
            # 表单验证不通过，打印出来错误信息
            print(form.errors.as_json())
            raise MyException(message="请输入正确的参数！")
            # return reponse_fail(message="请输入正确的参数！")

    def put(self, request, *args, **kwargs):
        body = request.body
        params = json.loads(body)

        form = user_forms.UserForms(params)
        result = form.is_valid()
        print(1111, result)
        if result:
            user = auth.authenticate(username=form.cleaned_data.get("username"),
                                     password=form.cleaned_data.get("password"))
            if user:
                # Dango自身方式设置session，持久化登陆
                # 创建一个session
                auth.login(request, user)
                # 获取设置的session值
                session = request.session.session_key
                return response_success({'session': session})
            else:
                raise MyException(message="登录失败！")
                # return reponse_fail(message="登录失败！")
        else:
            print(form.errors.as_json())
            raise MyException(message="请输入正确的用户名或者密码！")
            # return reponse_fail(message="请输入正确的用户名或者密码！")

# def register(request):
#     if request.method == "POST":
#         body = request.body
#         params = json.loads(body)
#         print(params)
#         form=user_forms.UserForms(params)
#         result=form.is_valid()
#         print(result)
#         if result:
#             # user=User.objects.create_user(username=str(params['username']),password=str(params['password']))
#             # 可以使用form.cleaned_data来获取对应的值，cleaned_data可以；理解为一个校验过的字典，和params一样的值
#             user=User.objects.create_user(username=form.cleaned_data.get("username"),
#                                           password=form.cleaned_data.get("password"))
#             if user:
#                 auth.login(request, user)
#                 # 获取设置的session值
#                 session = request.session.session_key
#                 return response_success()
#             else:
#                 return reponse_fail(message="添加用户失败！")
#         else:
#             #表单验证不通过，打印出来错误信息
#             print(form.errors.as_json())
#             return reponse_fail(message="请输入正确的参数！")
#     else:
#         return HttpResponse(404)
#
#
# def login_user(request):
#     if request.method == "POST":
#         body = request.body
#         params = json.loads(body)
#
#         form = user_forms.UserForms(params)
#         result = form.is_valid()
#         print(1111,result)
#         if result:
#             user=auth.authenticate(username=form.cleaned_data.get("username"),
#                                           password=form.cleaned_data.get("password"))
#             if user:
#                 # Dango自身方式设置session，持久化登陆
#                 #创建一个session
#                 auth.login(request, user)
#                 # 获取设置的session值
#                 session=request.session.session_key
#                 return response_success({'session':session})
#             else:
#                 return reponse_fail(message="登录失败！")
#         else:
#             print(form.errors.as_json())
#             return reponse_fail(message="请输入正确的用户名或者密码！")
#     else:
#         return HttpResponse(404)
#
#
# def get_user(request):
#     if request.method =="GET":
#         # 通过login(request,user)设置了session，可以通过request.user获取用户
#         token=request.META.get("HTTP_TOKEN",None)
#         print(token)
#         if token is None:
#             return reponse_fail(message="用户未登录")
#         else:
#             try:
#                 #根据head中的token获取session对象
#                 session=Session.objects.get(pk=token)
#             except Session.DoesNotExist:
#                 return reponse_fail(message="session失效")
#             except Exception as e:
#                 print(e)
#                 return reponse_fail(message="未知错误")
#             else:
#                 #固定写法，Django本身session获取user_id
#                 user_id=session.get_decoded().get('_auth_user_id',None)
#                 if user_id is None:
#
#                     return reponse_fail(message="用户ID失效！")
#                 try:
#                     user=User.objects.filter(pk=user_id).first()
#                     print(user.username)
#                 except User.DoesNotExist:
#                     return reponse_fail(message="用户不存在")
#
#                 return response_success(data={'username':user.username,'id':user.id})
#         # if user.is_authenticated:
#         #     return response_success(data={'username':user.username,'id':user.id})
#         # else:
#         #     return reponse_fail(message="用户未登录")
#     else:
#         return HttpResponse(404)
