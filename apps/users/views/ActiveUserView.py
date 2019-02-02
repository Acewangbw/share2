# _*_ coding: utf-8 _*_

from django.shortcuts import render
from users.forms.ActiveForm import ActiveForm
from repository.models import EmailVerifyRecord
from repository.models import UserProfile
import request



# 基于类实现需要继承的view
from django.views.generic.base import View

# 激活用户的view, 用于邮箱验证中使用到的激活连接的view。
class ActiveUserView(View):
    def get(self, request, active_code):
        # 查询邮箱验证记录是否存在
        all_record = EmailVerifyRecord.objects.filter(code=active_code)
        # 如果不为空也就是有用户
        active_form = ActiveForm(request.GET)
        if all_record:
            for record in all_record:
                # 获取到对应的邮箱
                email = record.email
                # 查找到邮箱对应的user
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
                # 激活成功跳转到登录页面
                return render(request, "login.html", )
        # 自己瞎输的验证码,下面的register.html 可以换成自定义的激活失败的提示页面，譬如register-fial.html,页面里面可以就写几个字。
        else:
            return render(
                request, "register.html", {
                    "msg": "您的激活链接无效", "active_form": active_form})
