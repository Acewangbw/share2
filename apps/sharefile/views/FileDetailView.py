# _*_ coding: utf-8 _*_
from django.http import HttpResponse

_author_ = 'Ace'
_date_ = '2019-02-02 13:54'

from django.shortcuts import render, redirect
from django.views.generic.base import View
from utils.mixin_utils import LoginRequiredMixin
from repository.models import AddFileModel, FilePublic,Process

from sharefile.forms.ProcessMaker import ProcessMaker



class FileDetailView(LoginRequiredMixin,View):
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self,request):
        print(request.GET)
        file_id = request.GET.get("id")
        print(file_id)
        file_obj = AddFileModel.objects.filter(nid=file_id)[0]
        print(file_obj)
        return render(request,'Ace-filedetail-realestate-add-property.html', {
            'file':file_obj
        })


    def post(self, request):

        print("post", request.POST)
        form_data = request.POST
        nid = form_data.get("nid")
        reason = form_data.get("keyword")
        is_review = form_data.get("is_review")
        print("是否通过：", is_review)
        file_obj = AddFileModel.objects.filter(nid=nid)[0]
        if is_review == "agree":
            status = 1
        elif is_review == "refuse":
            status = 2
        else:
            status = 0

        file_obj.reason = reason
        file_obj.status = status
        file_obj.save()


        return redirect('/')
        # return render(request, "index.html")


# def get(self, request):
    #     allfile = FilePublic.objects.filter()
    #     allfile = AddFileModel.objects.filter(nid=id,models_Filetype_type_id=2).only('nid','models_Filename','models_Filedes','models_Fileproject')
    #     if not allfile:
    #         return HttpResponse('已处理中的无法修改..')
    #     form = ProcessMaker(initial={'title': allfile.title, 'detail': allfile.detail})
    #
    #     return render(request,'Ace-filedetail-realestate-add-property.html',{'form':form,'nid':id)
    #
    # def post(self,request):
    #     form = ProcessMaker(data=request.POST)
    #     if form.is_valid():
    #         v = Process.objects.filter(nid=id,status=1).only('file_id','file__models_Filename','file__models_Filedes')
    #         if not v:
    #             return HttpResponse('已经被处理')
    #         else:
    #             return redirect('sharefile:filelist')
    #     return render(request, 'Ace-filedetail-realestate-add-property.html', {'form': form, 'nid': id})
