# _*_ coding: utf-8 _*_
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.contrib.auth.models import User
from users.forms.RegisterForm import RegisterForm

# 基于类实现需要继承的view
from django.views.generic.base import View

from repository.models import UserProfile
from utils.email_send import send_register_eamil

from django.contrib import auth
from django.contrib.auth.models import User


class RegisterView(View):
    # get方法直接返回页面
    def get(self, request):
        # 添加验证码
        register_form = RegisterForm()
        return render(
            request, "register.html", {
                'register_form': register_form})

    def post(self, request):
        # 实例化form
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            # 这里注册时前端的name为email
            user_email = request.POST.get("email", "")
            user_name = request.POST.get("username", "")
            user_password = request.POST.get("password", "")
            # print("-"*50)
            # print("user_name", user_name)
            # print("-" * 50)
            # 用户名查重
            if UserProfile.objects.filter(username=user_name):
                return render(
                    request, "register.html", {
                        "register_form": register_form, "msg": "用户已存在"})
            if UserProfile.objects.filter(email=user_email):
                return render(
                    request, "register.html", {
                        "register_form": register_form, "msg": "邮箱已经被占用了"})

            # 实例化一个user_profile对象，将前台值存入
            user_profile = UserProfile()


            user_profile.username = user_name
            user_profile.email = user_email

            # # 默认激活状态为false
            # user_profile.is_active = False

            # 加密password进行保存
            user_profile.password = make_password(user_password)
            user_profile.save()

            # 写入欢迎注册消息
            # user_message = UserMessage()
            # user_message.user = user_profile.id
            # user_message.message = "欢迎注册!! --系统自动消息"
            # user_message.save()
            # 发送注册激活邮件
            # send_register_eamil(user_email, "register")

            # 跳转到登录页面
            return render(request, "login.html", )
        # 注册邮箱form验证失败
        else:
            return render(
                request, "register.html", {
                    "register_form": register_form})