# _*_ coding: utf-8 _*_
# @Time     : 14:16
# @Author   : Amir
# @Site     : 
# @File     : adminx.py
# @Software : PyCharm

import xadmin
from xadmin import views
from .models import UserProfile, SystemUserProfile


class BaseSetting(object):
    # 添加主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    # 全局配置，后台管理标题和页脚
    site_title = "Amir"
    site_footer = "www.baidu.com"
    # 菜单收缩
    menu_style = "accordion"


class UserProfileAdmin(object):
    list_display = ['user', 'nickname', 'date_of_birth']


class SystemUserProfileAdmin(object):
    list_display = ['user', 'nickname', 'date_of_birth']


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(SystemUserProfile, SystemUserProfileAdmin)