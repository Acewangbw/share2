# _*_ coding: utf-8 _*_
_author_ = 'Ace'
_date_ = '2019-01-29 14:26'

from django.core.exceptions import ValidationError
from django import forms as django_forms
from django.forms import fields as django_fields
from  django import forms
from .base import BaseForm

# Way1
class LoginForm(forms.Form):
    # 用户名密码不能为空
    username = forms.CharField(required=True)
    # 密码不能小于5位
    password = forms.CharField(required=True, min_length=5)
    #记住密码
    rmb = django_forms.IntegerField(required=False)









