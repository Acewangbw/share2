# _*_ coding: utf-8 _*_
from repository.models import UserProfile

_author_ = 'Ace'
_date_ = '2019-02-09 16:04'
# 引入Django表单
from  django import forms
# 用于文件上传，修改头像

# class UploadImageForm(forms.Form):
#     image = forms.FileField(required=True)

class UploadImageForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['image']
