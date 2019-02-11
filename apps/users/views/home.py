#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 基于类实现需要继承的view
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.base import View
from repository.models import UserProfile



class homeview(LoginRequiredMixin,View):
    def get(self, request):

        user_info = UserProfile.objects.all()

        return render(request,'Ace-pages-profile.html',{'user_info':user_info})


