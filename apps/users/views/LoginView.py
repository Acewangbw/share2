# _*_ coding: utf-8 _*_




from django.contrib.auth import login, authenticate
from django.db.models import Q

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,redirect

# 基于类实现需要继承的view
from django.urls import reverse
from django.views.generic.base import View

from repository.models import UserProfile
from users.forms.LoginForm import LoginForm



#https://blog.csdn.net/zhangmengran/article/details/83547634
'''
尝试使用Absouble User试
'''

# Wa1 要匹配form
class LoginView(View):
    # 直接调用get方法免去判断
    def get(self, request):
        # render就是渲染html返回用户
        # render三变量: request 模板名称 一个字典写明传给前端的值
        redirect_url = request.GET.get('next', '')
        return render(request, "login.html", {
            "redirect_url": redirect_url
        })

    def post(self, request):
        result = {'status': False, 'message': None, 'data': None}
        # 类实例化需要一个字典参数dict:request.POST就是一个QueryDict所以直接传入
        # POST中的usernamepassword，会对应到form中
        login_form = LoginForm(request.POST)
        # 默认false
        request.session["is_login"] = False
        # is_valid判断我们字段是否有错执行我们原有逻辑，验证失败跳回login页面
        if login_form.is_valid():
            # 取不到时为空，username，password为前端页面name值
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            print("user_name", user_name, "pass_word", pass_word)

            # 成功返回user对象,失败返回null
            user = authenticate(username=user_name,password=pass_word)

            if user is not None:
                # 只有当用户激活时才给登录
                if user.is_active:
                    # login_in 两参数：request, user
                    # 实际是对request写了一部分东西进去，然后在render的时候：
                    # request是要render回去的。这些信息也就随着返回浏览器。完成登录
                    login(request, user)
                    # 跳转到首页 user request会被带回到首页
                    # 增加重定向回原网页。


                    # 存入session 序列化用户对象
                    user_dict = {}
                    user_ser = UserProfile.objects.filter(username=user_name)[0]
                    user_dict["is_admin"] = user_ser.is_admin
                    # user_dict["is_admin"] = user_ser.is_admin
                    # user_dict["is_approver"] = user_ser.is_approver
                    user_dict["is_approver"] = user_ser.is_approver
                    user_dict["user_name"] = user_ser.username
                    user_dict['user_id'] = user_ser.id
                    
                    request.session["user"] = user_dict
                    request.session["is_login"] = True
                    print("登录-----", user_dict)
                    # 增加重定向回原网页。

                    redirect_url = request.POST.get('next', '')
                    if redirect_url:
                        return HttpResponseRedirect(redirect_url)
                    # 跳转到首页 user request会被带回到首页
                    return HttpResponseRedirect(reverse("index"))
                # 即用户未激活跳转登录，提示未激活
                else:
                    return render(
                        request, "login.html", {
                            "msg": "用户名未激活! 请前往邮箱进行激活"})
            # 仅当用户真的密码出错时
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误!"})
        # 验证不成功跳回登录页面
        # 没有成功说明里面的值是None，并再次跳转回主页面
        else:
            return render(
                request, "login.html", {
                    "login_form": login_form})