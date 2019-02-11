# _*_ coding: utf-8 _*_
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse

from users.forms.ModifyPwdForm import ModifyPwdForm

_author_ = 'Ace'
_date_ = '2019-02-09 23:24'
# 基于类实现需要继承的view
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
import json

class UpdatePwdView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'next'

    def post(self, request):

        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            # # 如果两次密码不相等，返回错误信息
            if pwd1 != pwd2:
                return HttpResponse(
                    '{"status":"fail", "msg":"密码不一致"}',
                    content_type='application/json')
            # 如果密码一致
            user = request.user
            # 加密成密文
            user.password = make_password(pwd2)
            # save保存到数据库
            user.save()
            return HttpResponse(
                '{"status":"success"}',
                content_type='application/json')
        # 验证失败说明密码位数不够。
        else:
            # 通过json的dumps方法把字典转换为json字符串
            return HttpResponse(
                json.dumps(
                    modify_form.errors),
                content_type='application/json')