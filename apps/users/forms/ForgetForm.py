# _*_ coding: utf-8 _*_
# 引入Django表单
from  django import forms


# 忘记密码实现,这个是在点击忘记密码后要填写表单地方可以设定的提醒
class ForgetForm(forms.Form):
    # 此处email与前端name需保持一致。
    emailforget = forms.EmailField(required=True)
    # 应用验证码 自定义错误输出key必须与异常一样, 这里没设定
    # captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})