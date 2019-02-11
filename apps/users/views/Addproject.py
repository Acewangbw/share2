# _*_ coding: utf-8 _*_
from django.shortcuts import render, redirect
from django.views import View
from repository.models import ProjectModel
from users.forms.ProjectForm import ProjectForm


_author_ = 'Ace'
_date_ = '2019-02-02 19:51'

from django.shortcuts import render


def check_user(fun):

    print("装饰器验证是否已经登录。。。")

    def wrapper(self, request):
        # 从session获取用户信息
        try:
            user = request.session.get("user")
            return fun(self, request)
        except Exception as e:
            print("获取用户信息失败，用户未登录-------", e)
            return render(request, "login.html")

    return wrapper


class Addproject(View):
    def get(self,request):

        return render(request,'Ace-add-project.html')

    @check_user
    def post(self,request):

        project_form = ProjectForm(request.POST)

        project_profile = ProjectModel()

        if project_form.is_valid():
            project_profile.Project_name = request.POST.get("project", "")
            project_name = project_profile.Project_name
            print("创建项目-------, ", project_name)
            if ProjectModel.objects.filter(Project_name=project_name):
                return render(
                    request, "Ace-add-project.html", {
                        "project_form": project_form, "msg": "项目已存在"})

            project_profile.save()
        else:
            return render(
                request, "Ace-add-project.html", {
                    "project_form": project_form, "msg": "填写错误"})

        return redirect('index')



