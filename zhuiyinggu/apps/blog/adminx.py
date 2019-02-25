# _*_ coding: utf-8 _*_
# @Time     : 14:34
# @Author   : Amir
# @Site     : 
# @File     : adminx.py
# @Software : PyCharm

import xadmin
from .models import Blog


class BlogAdmin(object):
    list_display = ['title', 'subtitle', 'content', 'author', 'create_date', 'change_date', 'address']


xadmin.site.register(Blog, BlogAdmin)