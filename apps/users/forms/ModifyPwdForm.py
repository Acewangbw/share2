# _*_ coding: utf-8 _*_
# 引入Django表单
from  django import forms


# 重置密码form实现，这里是在点击邮件里面的链接后，跳转到修改密码页面里面需要填写表单的提醒
class ModifyPwdForm(forms.Form):
    # 密码不能小于5位
    password1 = forms.CharField(required=True, min_length=5)
    # 密码不能小于5位
    password2 = forms.CharField(required=True, min_length=5)