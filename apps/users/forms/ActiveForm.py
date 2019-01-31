# _*_ coding: utf-8 _*_
# 引入Django表单
from captcha.fields import CaptchaField
from  django import forms
# 激活时验证码实现
class ActiveForm(forms.Form):
    # 激活时不对邮箱密码做验证
    # 应用验证码 自定义错误输出key必须与异常一样
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})