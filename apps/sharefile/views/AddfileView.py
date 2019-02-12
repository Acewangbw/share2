# _*_ coding: utf-8 _*_
from datetime import datetime

from django.shortcuts import render, redirect

from sharefile.forms import AddfileForms
from repository.models import AddFileModel, U2D, UserProfile, File2DepModel
from repository.models import ProjectModel
from repository.models import Dep
from utils.mixin_utils import LoginRequiredMixin
from django.views.generic.base import View


class AddfileView(LoginRequiredMixin,View):
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self,request):
        dept = Dep.objects.all()
        project = ProjectModel.objects.all()

        return render(request,'Ace-file-add-realestate-add-property.html',{
            'dept':dept,
            'project': project,
        })
    #
    # def post(self,request):
    #     addfile_form = AddfileForms(request.POST)
    #
    #     file_profile = AddFileModel()
    #
    #     if addfile_form.is_valid():
    #         file_profile.models_Filename = request.POST.get("filename", "")
    #         file_profile.models_Filedepartment = request.POST.get("filedepartment", "")
    #         file_profile.models_Filedes = request.POST.get("filedes", "")
    #         file_profile.models_Fileusedfor = request.POST.get("fileusedfor", "")
    #
    #
    #         if 'fileupload' in list(request.FILES.keys()):
    #             file_profile.models_Fileupload = request.FILES['fileupload']
    #
    #
    #         file_profile.models_Updated_date = datetime.now()
    #         # 保存
    #         file_profile.save()
    #
    #         return redirect('/sharefile/filelist/')
    #
    #     else:
    #         return render(request, 'Ace-file-add-realestate-add-property.html')
    def post(self, request):

        try:

            # 从session获取用户信息
            user = request.session.get("user")
            print("user", user)
            user_name = user.get("user_name")
            # 传递到前端用于判断文件是否为当前用户
            user_id = user.get("user_id")
            # 查询对应用户信息
            user_obj = UserProfile.objects.filter(id=user_id)[0]
            print("用户对象: ", user_obj)
            # user_obj = UserProfile.objects.filter(id=user_id)
        except AttributeError as e:
            print("获取用户信息失败，用户未登录-------", e)
            return render(request, "login.html")

        print("添加文件")
        print("*"*20)
        print(request.POST)
        addfile_from = request.POST
        if addfile_from :
            # 文件名
            filename = addfile_from.get("filename")
            # 文件描述
            filedes = addfile_from.get("filedes")
            # 文件类型
            filetype = addfile_from.get('filetype')
            # 项目
            fileproject = addfile_from.get('fileproject')
            # 部门
            deps = addfile_from.getlist("dep")
            print("选择的部门", deps)

            dep_obj_list = []
            for dep in deps:
                print(Dep.objects.filter(title=dep))
                dep_obj_list.append(Dep.objects.filter(title=dep)[0])
            print("部门对象列表: ", dep_obj_list)
            if 'fileupload' in list(request.FILES.keys()):
                fileupload = request.FILES['fileupload']
            else:
                fileupload = None

            if filetype == "外部":
                filetype_id = 1
            elif filetype == "内部":
                filetype_id = 2
            else:
                filetype_id = 2

            # 查询对应的项目
            project = ProjectModel.objects.filter(Project_name=fileproject)
            print("project: ", project)
            print(project[0].nid)
            file_profile = AddFileModel()
            file_profile.models_Filename = filename
            file_profile.models_Filedes = filedes
            file_profile.models_Filetype_type_id = filetype_id
            file_profile.models_Fileproject = project[0]
            file_profile.models_Fileupload = fileupload
            file_profile.models_Updated_date = datetime.now()
            file_profile.user_id = user_obj
            # 保存
            file_profile.save()

            # 多部门添加
            for dep_obj in dep_obj_list:

                file_dep = File2DepModel()
                file_dep.dep = dep_obj
                file_dep.file = file_profile
                file_dep.save()

            return redirect('/sharefile/filelist/')

        else:
            return render(request, 'Ace-file-add-realestate-add-property.html')
