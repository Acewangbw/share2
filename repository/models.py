# _*_ coding: utf-8 _*_
from datetime import datetime

from django.contrib.auth.models import AbstractUser

_author_ = 'Ace'
_date_ = '2019-01-29 14:24'

from django.db import models


class UserInfo(models.Model):
    """
    用户表
    """

    nid = models.BigAutoField(primary_key=True)
    username = models.CharField(verbose_name='用户名', max_length=32, unique=True)
    password = models.CharField(verbose_name='密码', max_length=64)
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称")
    email = models.EmailField(verbose_name='邮箱', unique=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # 头像 默认使用default.png
    image = models.ImageField(
        upload_to="image/%Y/%m",
        default=u"image/default.png",
        max_length=100,
        verbose_name=u"头像"
    )

    # 是否有权限 0 没有 1 有
    is_admin = models.BooleanField(null=False, default=False)


    is_active = models.BooleanField(null=False, default=False)

    # meta信息，即后台栏目名
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    # 重载__str__方法，打印实例会打印username，username为继承自AbstractUser
    def __str__(self):
        return self.username

    def set_password(self, pass_word):
        pass


# Way 3 logintest
# class UserInfo(AbstractUser):
#     """
#     用户表
#     """
#
#     nid = models.BigAutoField(primary_key=True)
#     # username = models.CharField(verbose_name='用户名', max_length=32, unique=True)
#     # password = models.CharField(verbose_name='密码', max_length=64)
#     nick_name = models.CharField(max_length=50, verbose_name=u"昵称")
#     email = models.EmailField(verbose_name='邮箱', unique=True)
#     create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
#     # 头像 默认使用default.png
#     image = models.ImageField(
#         upload_to="image/%Y/%m",
#         default=u"image/default.png",
#         max_length=100,
#         verbose_name=u"头像"
#     )
#
#     # 是否有权限 0 没有 1 有
#     is_admin = models.BooleanField(null=False, default=False)
#
#
#     # is_active = models.BooleanField(('active'),default=True,)
#
#     # meta信息，即后台栏目名
#     class Meta:
#         verbose_name = "用户信息"
#         verbose_name_plural = verbose_name
#
#     # 重载__str__方法，打印实例会打印username，username为继承自AbstractUser
#     def __str__(self):
#         return self.username




class Dep(models.Model):
    """
    博客信息
    """
    nid = models.BigAutoField(primary_key=True)
    title = models.CharField(verbose_name='个人博客标题', max_length=64)
    site = models.CharField(verbose_name='个人博客前缀', max_length=32, unique=True)
    # theme = models.CharField(verbose_name='博客主题', max_length=32)
    user = models.OneToOneField(to='UserInfo', to_field='nid',on_delete=models.CASCADE)

class U2D(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, null=True, verbose_name='用户所属部门')
    dep = models.ForeignKey(Dep, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = u"用户2部门"

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.user



class Project(models.Model):
    nid = models.AutoField(primary_key=True)
    Project_name = models.CharField(verbose_name='项目名称', max_length=32)
    dep = models.ForeignKey(verbose_name='所属博客', to='Dep', to_field='nid',on_delete=models.CASCADE)


class AddFileModel(models.Model):

    nid = models.BigAutoField(primary_key=True)
    models_Filename = models.CharField(max_length=20, verbose_name=u"文件名称", default='')
    models_Filedes = models.TextField(verbose_name=u"描述", default='')
    read_count = models.IntegerField(default=0)

    models_Fileupload = models.FileField(
        upload_to="file/%Y/%m",
        verbose_name=u"文件",
        max_length=1000, )

    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)


    department = models.ManyToManyField(
        to="Dep",
        through="File2DepModel",
        through_fields=('file', 'dep'),
    )


    class Meta:
        verbose_name = u"上传文件"
        verbose_name_plural = verbose_name



#定义部门
class File2DepModel(models.Model):

    file = models.ForeignKey(AddFileModel,on_delete=models.CASCADE,null=True,verbose_name='文章到部门')
    dep = models.ForeignKey(Dep,on_delete=models.CASCADE,null=True,verbose_name='部门')


    class Meta:
        verbose_name_plural = u"文件2部门"

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.file

# 邮箱验证码model
class EmailVerifyRecord(models.Model):
    SEND_CHOICES = (
        ("register", u"注册"),
        ("forget", u"找回密码"),
        ("update_email", u"修改邮箱"),
    )
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    # 未设置null = true blank = true 默认不可为空
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(choices=SEND_CHOICES, max_length=20, verbose_name=u"验证码类型")
    # 这里的now得去掉(),不去掉会根据编译时间。而不是根据实例化时间。
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u"发送时间")

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    # 重载str方法使后台不再直接显示object
    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)




