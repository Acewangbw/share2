# _*_ coding: utf-8 _*_
from django.shortcuts import render

from users.forms.ActiveForm import ActiveForm
from users.forms.ForgetForm import ForgetForm

from utils.email_send import send_register_eamil



# 基于类实现需要继承的view
from django.views.generic.base import View


# 用户忘记密码的处理view, 找个页面和index页面放在一起了
class ForgetPwdView(View):
    # get方法直接返回页面
    def get(self, request):
        # 给忘记密码页面加上验证码
        active_form = ActiveForm(request.POST)
        # return render(request, "forgetpwd.html", {"active_form": active_form})
        return render(request, "login.html", {"active_form": active_form})
    # post方法实现

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        # form验证合法情况下取出email
        if forget_form.is_valid():
            email = request.POST.get("emailforget", "")
            # 发送找回密码邮件, 这里的forget是应该是返回的页面
            send_register_eamil(email, "forget")
            # 发送完毕返回登录页面并显示发送邮件成功。
            return render(request, "login.html", {"msg": "重置密码邮件已发送,请注意查收"})
        # 如果表单验证失败也就是他验证码输错等。
        else:
            return render(
                request, "login.html", {
                    "forget_from": forget_form})
            # return render(
            #     request, "forgetpwd.html", {
            #         "forget_from": forget_form})