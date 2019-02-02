# _*_ coding: utf-8 _*_
from django.contrib.auth.hashers import make_password
from django.shortcuts import render

from users.forms.ModifyPwdForm import ModifyPwdForm
from repository.models import UserProfile

_author_ = 'Ace'
_date_ = '2019-01-16 11:54'
# 基于类实现需要继承的view
from django.views.generic.base import View



# 改变密码的view, 这里时为了，接收到邮件链接后，点击进入修改密码页面，进行重置密码的页面的view
class ModifyPwdView(View):
    def post(self, request):
        modiypwd_form = ModifyPwdForm(request.POST)
        if modiypwd_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            email = request.POST.get("email", "")
            # 如果两次密码不相等，返回错误信息
            if pwd1 != pwd2:
                return render(
                    request, "reset_pwd.html", {
                        "email": email, "msg": "密码不一致"})
            # 如果密码一致
            user = UserProfile.objects.get(email=email)
            # 加密成密文
            user.password = make_password(pwd2)
            # save保存到数据库
            user.save()
            return render(request, "login.html", {"msg": "密码修改成功，请登录"})
        # 验证失败说明密码位数不够。
        else:
            email = request.POST.get("email", "")
            return render(
                request, "reset_pwd.html", {
                    "email": email, "modiypwd_form": modiypwd_form})