"""EdmureBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path

from users.views.UpdatePwdView import UpdatePwdView
# from users.views.UploadImageView import UploadImageView
from users.views.home import homeview
from users.views.Addproject import Addproject
from users import views
from users.views.UploadImageView import Upload_image


app_name = 'users'
# urlpatterns = [
#     path('register',RegisterView.as_view,name='profile')
# ]


urlpatterns = [
        path('home/', homeview.as_view(), name='home'),
        path('addproject/', Addproject.as_view(), name='addproject'),
        path('imageupload/', views.UploadImageView.Upload_image ),# 用户头像上传
        # 用户个人中心修改密码
        path('update/pwd/', UpdatePwdView.as_view(), name="update_pwd"),
        ]