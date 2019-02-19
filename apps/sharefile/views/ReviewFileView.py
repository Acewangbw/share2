from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.base import View

from repository.models import AddFileModel, U2D, UserProfile
from django.db.models import Q


class ReviewFileView(View):


    def get(self, request):

        try:
            #从session获取用户信息
            user = request.session.get("user")
            print("user", user)
            user_name = user.get("user_name")
            # 传递到前端用于判断文件是否为当前用户
            user_id = user.get("user_id")
            #查询对应用户信息
            user_obj = UserProfile.objects.filter(id=user_id)[0]
            print("用户对象: ", user_obj)
            # user_obj = UserProfile.objects.filter(id=user_id)
        except AttributeError as e:
            print("获取用户信息失败，用户未登录-------",e)
            return render(request, "login.html")


        # 查询所有未审核和未通过的文件
        all_file = AddFileModel.objects.filter(~Q(status=1) & Q(models_Filetype_type_id=1))
        # all_file = AddFileModel.objects.filter(~Q(status=1) & Q(models_Filetype_type_id=1))

        #Ace - processlist - table - basic.html

        return render(request, 'Ace-processlist-table-basic.html', {
            'allfile': all_file
        })

    #
    # def post(self, request):
    #
    #     pass