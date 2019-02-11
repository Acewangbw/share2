# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.views import View

_author_ = 'Ace'
_date_ = '2019-02-03 12:25'

class ProcessView(View):
    def get(self,request):
        return render(request,'Ace-processlist-table-basic.html')
