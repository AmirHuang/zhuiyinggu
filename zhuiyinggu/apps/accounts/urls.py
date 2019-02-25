# _*_ coding: utf-8 _*_
# @Time     : 11:56
# @Author   : Amir
# @Site     : 
# @File     : urls.py
# @Software : PyCharm

from django.conf.urls import url, re_path
from accounts import views

urlpatterns = [
    re_path(r'^gettoken/', views.GetToken.as_view()),
]