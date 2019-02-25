# _*_ coding: utf-8 _*_
# @Time     : 14:23
# @Author   : Amir
# @Site     : 
# @File     : adminx.py
# @Software : PyCharm

import xadmin
from .models import ApkVersion


class ApkVersionAdmin(object):
    # 显示的列
    list_display = ['name', 'version', 'creator', 'create_date', 'address']


xadmin.site.register(ApkVersion, ApkVersionAdmin)