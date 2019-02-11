# _*_ coding: utf-8 _*_
from sharefile.views.FileDetailView import FileDetailView

_author_ = 'Ace'
_date_ = '2019-01-30 15:57'


from sharefile.views.AddfileView import AddfileView
from sharefile.views.FileListView import FileListView
from sharefile.views.ProjectListView import ProjectListView
from sharefile.views.ProccessView import ProcessView
from sharefile.views.ReviewFileView import ReviewFileView

from django.urls import path, include, re_path
# from . import views


app_name = 'sharefile'


urlpatterns = [
        path('addfile/', AddfileView.as_view(), name='addfile'),
        path('filelist/', FileListView.as_view(), name='filelist'),
        path('filedetail/', FileDetailView.as_view(), name='filedetail'),
        path('process/', ProcessView.as_view(), name='process'),
        path('project_list/',ProjectListView.as_view(), name='project'),
        path('review/', ReviewFileView.as_view(), name="review")
        # re_path('filelist/(?P<pk>\d+)/',FileListView.as_view(), name='filelist'),
        # re_path('filedownload/(?P<product_id>\d+)/', CountDownloadView.as_view, name='countdownload'),
        # path('buttons/', ButtonsView.as_view(), name='buttons'),
        # path('edit/', EditView.as_view(), name='edit'),
        # path('wheel/', WheelView.as_view(), name='wheel'),
        #删除
        # path(r'^del-file/$', views.del_file, name="del_file"),
        # path('delete_file/',views.del_file, name='delete_file'),
        ]
