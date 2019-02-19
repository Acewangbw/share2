# _*_ coding: utf-8 _*_
from django.db.models import Q
from django.shortcuts import render, redirect

# 基于类实现需要继承的view
from django.views.generic.base import View

from repository.models import AddFileModel, Dep, ProjectModel, File2DepModel, U2D, FilePublic
from repository.models import UserProfile
from utils.mixin_utils import LoginRequiredMixin


# Way1
class Index(View):
    # login_url = '/login/'
    # redirect_field_name = 'next'

    def get(self,request):

        try:
            # 从session获取用户信息, 如果不存在会报空指针异常，代表用户未登录
            user = request.session.get("user")
            user_name = user.get("user_name")
            allfile = AddFileModel.objects.filter(Q(models_Filetype_type_id=1) & Q(status=1))

        except Exception as e:
            print("----访问主页异常----", e)
            #这里要进行判断
            # file = FilePublic.objects.filter(status=1)
            #这里之后要删掉的。
            allfile = AddFileModel.objects.filter(Q(models_Filetype_type_id=1) & Q(status=1))

            allproject = ProjectModel.objects.all()
            print(allproject)

            return render(request, 'Ace-dashboard-table-basic.html', {'allfile': allfile,
                                                                      'allproject':allproject,
                                                                      })
        #
        # # 查询对应用户信息
        # # ? 这里需要把File2DepModel表里面的数据拿出来，然后筛选文件所属部门，进行显示。
        # user_obj = U2D.objects.filter(user=user_name)[0]
        # dep_id = user_obj.dep_id
        # # #如何设定将文件共享的和部门内部共享，在登陆后都可以一起显示出来，还要将数据按最新的排序。
        # allfile =File2DepModel.objects.filter(dep=dep_id)

        allproject = ProjectModel.objects.all()
        print(allproject)

        return render(request, 'Ace-dashboard-table-basic.html', {
                'allfile': allfile,
                'allproject':allproject,
            })








    # Feb 17 之前的
# class Index(View):
#     # login_url = '/login/'
#     # redirect_field_name = 'next'
#
#     def get(self,request):
#
#         try:
#             # 从session获取用户信息, 如果不存在会报空指针异常，代表用户未登录
#             user = request.session.get("user")
#             user_name = user.get("user_name")
#
#         except Exception as e:
#             print("----访问主页异常----", e)
#             #这里要进行判断
#             # file = FilePublic.objects.filter(status=1)
#             #这里之后要删掉的。
#             allfile = AddFileModel.objects.filter(Q(models_Filetype_type_id=1) & Q(status=1))
#
#             allproject = ProjectModel.objects.all()
#             print(allproject)
#
#             return render(request, 'Ace-dashboard-table-basic.html', {'allfile': allfile,
#                                                                       'allproject':allproject,
#                                                                       })
#         #
#         # # 查询对应用户信息
#         # # ? 这里需要把File2DepModel表里面的数据拿出来，然后筛选文件所属部门，进行显示。
#         # user_obj = U2D.objects.filter(user=user_name)[0]
#         # dep_id = user_obj.dep_id
#         # # #如何设定将文件共享的和部门内部共享，在登陆后都可以一起显示出来，还要将数据按最新的排序。
#         # allfile =File2DepModel.objects.filter(dep=dep_id)
#
#         allproject = ProjectModel.objects.all()
#         print(allproject)
#
#         return render(request, 'Ace-dashboard-table-basic.html', {
#                 # 'allfile': allfile,
#             'allproject':allproject,
#             })



