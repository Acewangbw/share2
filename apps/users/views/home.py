#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 基于类实现需要继承的view
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.base import View



class homeview(LoginRequiredMixin,View):
    def get(self, request):
        return render(request,'Ace-pages-profile.html')


