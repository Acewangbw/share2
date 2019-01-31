# _*_ coding: utf-8 _*_
from django.shortcuts import render

from repository.models import EmailVerifyRecord

_author_ = 'Ace'
_date_ = '2019-01-16 11:53'
# 基于类实现需要继承的view
from django.views.generic.base import View


# 重置密码的view,这里的view是为了设定点击忘记密码后需要发送邮件的view
class ResetView(View):
    def get(self, request, active_code):
        # 查询邮箱验证记录是否存在
        all_record = EmailVerifyRecord.objects.filter(code=active_code)
        # 如果不为空也就是有用户
        # active_form = ActiveForm(request.GET)
        if all_record:
            for record in all_record:
                # 获取到对应的邮箱
                email = record.email
                # 将email传回来
                return render(request, "reset_pwd.html", {"email": email})
        # 自己瞎输的验证码
        else:
            return render(
                request, "login.html", {
                    "msg": "您的重置密码链接无效,请重新请求", "active_form": active_form})