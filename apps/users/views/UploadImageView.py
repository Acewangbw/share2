# _*_ coding: utf-8 _*_
from django.shortcuts import render

from share2 import settings
from users.forms.UploadImageForm import UploadImageForm

_author_ = 'Ace'
_date_ = '2019-02-09 16:05'
# 基于类实现需要继承的view
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from repository.models import UserProfile
from django.http import HttpResponseRedirect, HttpResponse
# 用户上传图片的view:用于修改头像
import json
import uuid
import os


def Upload_image(request):
    response = {'status': True, 'message': None, 'data': None}
    if request.method == 'POST':
        # 前端ajax请求，将图片对象、图片名称传递到了后台的views.py中；
        img = request.FILES.get('img_file')

        # 获取数据库head_img字段的值，并切割成列表。
        # ['2018', '10', 'h2.png']
        # path = request.user.image.url.split('/')
        # path = request.user.image.strip()
        img_name = request.POST.get('img_name')
        print(img_name)
        # 将列表的最后一个元素图片名称，替换成新的图片名称
        # path[-1] = request.POST.get('img_name')
        #
        # # 再将列表合成一个字符串
        # path = '/'.join(path)
        # print(path,'打印路径')



        # url = settings.MEDIA_ROOT
        # url = path
        # url = "/"+ path
        url = settings.MEDIA_ROOT +"/avatar/"+ img_name #Orignal one
        # path = url
        # url = settings.MEDIA_ROOT +"/"+ path #Orignal one
        # url = os.path.join('static/images/avatar', path)

        # 将ajax传过来的图片写入到本地/static/images/....目录下。
        with open(url, 'wb') as f:
            for chunk in img.chunks():
                f.write(chunk)

        # 以上步骤实现了图片的后台保存，还需要修改当前用户数据库中的头像路径。
        request.user.image = img
        request.user.save()

        return HttpResponse('头像上传成功')



#
# Feb 11 只能上传文件
# def Upload_image(request):
#     response = {'status': True, 'message': None, 'data': None}
#     # print(request.POST)
#     try:
#         user_image = request.POST.get('image')
#         obj = UserProfile.objects.update(image=user_image)
#         # user_image = request.POST.get('image')
#         # file_name = str(uuid.uuid4())
#         # file_path = os.path.join('static/images/avatar', file_name)
#         # f = open(file_path, 'wb')
#         # for chunk in user_image.chunks():
#         #     f.write(chunk)
#         # f.close()
#
#
#
#         # obj = UserProfile.objects.update(
#         #     image=user_image
#         # )
#
#         response['data'] = obj.id
#         response['status'] = True
#
#     except Exception as e:
#         response['status'] = False
#         response['message'] = '上传错误'
#
#     result = json.dumps(response, ensure_ascii=False)
#     return HttpResponse(result)












# class UploadImageView(LoginRequiredMixin, View):
#     login_url = '/login/'
#     redirect_field_name = 'next'

    # def get(self,request):
    #     return render(request,'Tools-anybuttons-ui-buttons.html')

    # def post(self, request):
    #     # 这时候用户上传的文件就已经被保存到imageform了 ，为modelform添加instance值直接保存
    #     # image_form = UploadImageForm(
    #     #     request.POST, request.FILES)
    #
    #     image_form = UploadImageForm(request.POST,request.FILES,instance=request.user)
    #
    #     if image_form.is_valid():
    #
    #
    #
    #         image_form.save()
    #         # # 取出cleaned data中的值,一个dict
    #         # image = image_form.cleaned_data['image']
    #         # request.user.image = image
    #         # request.user.save()
    #         return HttpResponse(
    #             '{"status":"success"}',
    #             content_type='application/json')
    #     else:
    #         return HttpResponse(
    #             '{"status":"fail"}',
    #             content_type='application/json')