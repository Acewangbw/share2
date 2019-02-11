# _*_ coding: utf-8 _*_
from django.shortcuts import render, redirect
from django.views.generic.base import View

from repository.models import AddFileModel, U2D
from repository.models import UserProfile
from utils.mixin_utils import LoginRequiredMixin



class FileListView(LoginRequiredMixin,View):
    login_url = '/login/'
    redirect_field_name = 'next'

    # def get(self, request):


        # return render(request,'Ace-filelist-transaction-listing.html')

    #

    def get(self,request):
        try:

            #从session获取用户信息
            user = request.session.get("user")
            print("user", user)
            user_name = user.get("user_name")
            # 传递到前端用于判断文件是否为当前用户
            user_id = user.get("user_id")
            #查询对应用户信息
            user_obj = U2D.objects.filter(user_id=user_id)[0]
            print("用户对象: ", user_obj)
            # user_obj = UserProfile.objects.filter(id=user_id)
        except AttributeError as e:
            print("获取用户信息失败，用户未登录-------",e)
            return render(request, "login.html")
        #部门id
        dep_id = user_obj.dep_id
        dep_name = user_obj.dep
        #查询部门对应的文件
        allfile = AddFileModel.objects.filter(department_id=dep_id)
        # allfile = AddFileModel.objects.filter(department_id=dep_id)
        print("8"*10)
        print(allfile)
        #allfile = AddFileModel.objects.all()
       # countfile = AddFileModel.objects.count()
        countfile = len(allfile)

        # user_obj = UserProfile.objects.get(username=username)

        return render(request,'Ace-filelist-transaction-listing.html',{
            'allfile':allfile,
            'countfile':countfile,
            'user_id':user_id
        })

    def post(self,request):

        file_id = request.POST['file_id'] #找到对应文件的ID。
        op = request.POST['op'] #找到前端中标记出来的操作。
        if 'del' == op: #找寻操作用，可以用于区别编辑内容。
            try:
                r = AddFileModel.objects.filter(id=int(file_id))#筛选出ID。
                r.delete()#删除
                # global status
                # status = 'del success'
                return redirect('/sharefile/filelist/')
            except:
                # global status
                # status = 'del failed'
                return redirect('/sharefile/filelist/')
                pass

        return redirect('/sharefile/filelist/')