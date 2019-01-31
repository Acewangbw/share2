# _*_ coding: utf-8 _*_
_author_ = 'Ace'
_date_ = '2019-01-29 14:28'


from django import forms as django_forms
from django.forms import fields as django_fields


from .base import BaseForm

# class RegisterForm(BaseForm, django_forms.Form):
#     username = django_fields.CharField()
#     password = django_fields.CharField()
#     confirm_pwd = django_fields.CharField()
#
#     def clean(self):
#         v1 = self.cleaned_data['password']
#         v2 = self.cleaned_data['confirm_pwd']
#         if v1 == v2:
#             pass
#         else:
#             from django.core.exceptions import ValidationError,NON_FIELD_ERRORS
#             raise ValidationError('密码输入不一致')

from captcha.fields import CaptchaField
from  django import forms

# 验证码form & 注册表单form
class RegisterForm(forms.Form):
    # 此处email与前端name需保持一致。
    email = forms.EmailField(required=True)
    #账号
    account = forms.CharField(required=True)
    # 密码不能小于5位
    password = forms.CharField(required=True)
    # 应用验证码 自定义错误输出key必须与异常一样
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})
