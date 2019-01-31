# _*_ coding: utf-8 _*_
from django.shortcuts import render, redirect

# 基于类实现需要继承的view
from django.views.generic.base import View

from repository.models import AddFileModel, Dep, Project
from repository.models import UserInfo
from utils.mixin_utils import LoginRequiredMixin


# Way1
class Index(View):
    # login_url = '/login/'
    # redirect_field_name = 'next'

    def get(self,request):

        try:
            # 从session获取用户信息
            user = request.session.get("user")
            user_name = user.get("user_name")
        except:
            return render(request, 'Ace-dashboard-table-basic.html')
            pass
            # 查询对应用户信息
        user_obj = UserInfo.objects.filter(username=user_name)[0]
        # 部门id
        dep_id = user_obj.department_id
        # 查询部门对应的文件
        allfile = AddFileModel.objects.filter(department_id=dep_id)
        #
        # if allfile:


        return render(request, 'Ace-dashboard-table-basic.html', {
                'allfile': allfile,
            })


# Way2 Login

# class Index(View):
#     def get(self, request,site):
#         dep = Dep.objects.filter(site=site).select_related('user').first()
#         if not dep:
#             return redirect('/')
#         project_list = Project.objects.filter(dep=dep)
#         # tag_list = models.Tag.objects.filter(blog_id=blog.nid)
#         # category_list = models.Category.objects.filter(blog=blog)
#
#         # data_list = AddFileModel.objects.raw('select nid, count(nid) as nm,strftime("%Y-%m",create_time) as ctime from repository_article group by strftime("%Y-%m",create_time)')
#
#         file_list = AddFileModel.objects.filter(dep=dep).order_by('-nid').all()
#
#         return render(
#             request,
#             'Ace-dashboard-table-basic.html',
#             {
#                 'dep': dep,
#                 'project_list': project_list,
#                 # 'data_list': data_list,
#                 'file_list': file_list
#             }
#         )