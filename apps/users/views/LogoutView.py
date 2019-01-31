# _*_ coding: utf-8 _*_
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse

_author_ = 'Ace'
_date_ = '2019-01-16 11:54'
# 基于类实现需要继承的view
from django.views.generic.base import View


class LogoutView(View):
    def get(self, request):
        request.session.clear()
        # django自带的logout
        logout(request)
        # 重定向到首页,
        return HttpResponseRedirect(reverse("login"))