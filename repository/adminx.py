# _*_ coding: utf-8 _*_
_author_ = 'Ace'
_date_ = '2019-02-02 8:08'

import xadmin
# 和X admin的view绑定
from xadmin import views

from repository.models import Dep, U2D, File2DepModel, ProjectModel, AddFileModel


# X admin的全局配置信息设置
class BaseSetting(object):
    # 主题功能开启
    enable_themes = True
    use_bootswatch = True

#将Xadmin全局管理器与我们的view绑定注册。
xadmin.site.register(views.BaseAdminView, BaseSetting)

# x admin 全局配置参数信息设置
class GlobalSettings(object):
    site_title = "学校文件上传系统"
    site_footer = "Created by Ace"
    # 收起菜单
    # menu_style = "accordion"

# 将头部与脚部信息进行注册:
xadmin.site.register(views.CommAdminView, GlobalSettings)


class DepAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['nid', 'title', 'site']
    # 配置搜索字段,不做时间搜索
    search_fields = ['nid', 'title', 'site']
    # 配置筛选字段
    list_filter = ['nid', 'title', 'site']
xadmin.site.register(Dep, DepAdmin)


class U2DAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['user', 'dep']
    # 配置搜索字段,不做时间搜索
    search_fields = ['user', 'dep']
    # 配置筛选字段
    list_filter = ['user', 'dep']
xadmin.site.register(U2D, U2DAdmin)

class ProjectModelAdmin(object):
    # # 配置后台我们需要显示的列
    # list_display = ['nid', 'Project_name','dep']
    # # 配置搜索字段,不做时间搜索
    # search_fields = ['nid', 'Project_name','dep']
    # # 配置筛选字段
    # list_filter = ['nid', 'Project_name','dep']
    # 配置后台我们需要显示的列
    list_display = ['nid', 'Project_name']
    # 配置搜索字段,不做时间搜索
    search_fields = ['nid', 'Project_name']
    # 配置筛选字段
    list_filter = ['nid', 'Project_name']

xadmin.site.register(ProjectModel, ProjectModelAdmin)

class File2DepModelAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['file', 'dep']
    # 配置搜索字段,不做时间搜索
    search_fields = ['file', 'dep']
    # 配置筛选字段
    list_filter = ['file', 'dep']
xadmin.site.register(File2DepModel, File2DepModelAdmin)

class AddFileModelAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['nid', 'models_Filename','models_Filedes',
                    'read_count','models_Fileupload',
                    'create_time','department','models_Filetype_type_id','models_Fileproject']
    # 配置搜索字段,不做时间搜索
    search_fields = ['nid', 'models_Filename','models_Filedes',
                    'read_count','models_Fileupload',
                    'create_time','department','models_Filetype_type_id','models_Fileproject']
    # 配置筛选字段
    list_filter = ['nid', 'models_Filename','models_Filedes',
                    'read_count','models_Fileupload',
                    'create_time','department','models_Filetype_type_id','models_Fileproject']

xadmin.site.register(AddFileModel, AddFileModelAdmin)