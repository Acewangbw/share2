# _*_ coding: utf-8 _*_
from django.shortcuts import render, redirect
from django.views.generic.base import View

from repository.models import AddFileModel, U2D,File2DepModel
from repository.models import UserProfile
from utils.mixin_utils import LoginRequiredMixin



class FileListView(LoginRequiredMixin,View):
    login_url = '/login/'
    redirect_field_name = 'next'


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
        print(dep_id)

        allfile = File2DepModel.objects.filter(dep_id=dep_id)
        # file_all = allfile.all()


        # file_id = allfile.all()
        # print(allfile.all(),'Ace test for fild id')


        # print(allfile.model.file.id)

        # print(file_obj)
        # print(file_obj[0],"测试1")
        # print(file_obj[0].file,"测试2")
        #
        # print(type(file_obj[0]),"测试类型1")
        # print(type(file_obj[0].file), "测试类型2")

        # file_id = AddFileModel.objects.filter(nid=file_id)
        #


        # dep_name = user_obj.dep
        # # dep_id =File2DepModel.objects
        # #获取File2Dep表里面的文件ID。
        # file_id2 = File2DepModel.objects.filter(dep=dep_id2) #Modify2
        # fileid = file_id2.model.dep.id
        # dep_name = user_obj.dep
        # #查询部门对应的文件
        # allfile = AddFileModel.objects.filter(fild_id=file_id)#Modify 1
        #获取文件表里面的文件
        # allfile = AddFileModel.objects.filter(nid=file_obj)  # Modify 1

        # allfile = File2DepModel.objects.filter(dep_id=dep_id)#Modify 2



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
            'user_id':user_id,
            # 'file_all':file_all
        })



    # def post(self,request):
    #
    #     file_id = request.POST['file_id'] #找到对应文件的ID。
    #     op = request.POST['op'] #找到前端中标记出来的操作。
    #     if 'del' == op: #找寻操作用，可以用于区别编辑内容。
    #         try:
    #             r = AddFileModel.objects.filter(id=int(file_id))#筛选出ID。
    #             r.delete()#删除
    #             # global status
    #             # status = 'del success'
    #             return redirect('/sharefile/filelist/')
    #         except:
    #             # global status
    #             # status = 'del failed'
    #             return redirect('/sharefile/filelist/')
    #             pass






    #
    # def post(self,request):
    #
    #     file_id = request.POST.get['file_id'] #找到对应文件的ID。
    #     op = request.POST.get['op'] #找到前端中标记出来的操作。
    #     if 'del' == op: #找寻操作用，可以用于区别编辑内容。
    #         try:
    #             r = AddFileModel.objects.filter(id=int(file_id))#筛选出ID。
    #             r.delete()#删除
    #             # global status
    #             # status = 'del success'
    #             return redirect('/sharefile/filelist/')
    #         except:
    #             # global status
    #             # status = 'del failed'
    #             return redirect('/sharefile/filelist/')
    #             pass
    #
    #     return redirect('/sharefile/filelist/')