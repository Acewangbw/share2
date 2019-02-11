# _*_ coding: utf-8 _*_
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic.base import View

from repository.models import AddFileModel, U2D, ProjectModel
from repository.models import UserProfile




class ProjectListView(View):


    def get(self,request):
        try:
            # 从session获取用户信息
            user = request.session.get("user")
            p_id = request.GET.get("id")
            # 查询项目内的文件并且公开
            all_file = AddFileModel.objects.filter(models_Fileproject=p_id)
            print("查询所有的项目分类文件: ", all_file)
        except Exception as e:
            all_file = []
            print("用户未登录", e)
            p_id = request.GET.get("id")
            # 查询项目内的文件并且公开
            all_file = AddFileModel.objects.filter(Q(models_Fileproject=p_id) & Q(models_Filetype_type_id=1) & Q(status=1))
            print("查询所有的项目分类文件: ", all_file)

        countfile = len(all_file)
        return render(request,'Ace-filelist-transaction-listing.html',{
            'allfile':all_file,
            'countfile':countfile
        })
