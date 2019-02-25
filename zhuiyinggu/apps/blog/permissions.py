# _*_ coding: utf-8 _*_
# @Time     : 13:41
# @Author   : Amir
# @Site     : 
# @File     : permissions.py
# @Software : PyCharm

"""
blog/permissions.py

权限：
IsAuthenticatedOrReadOnly
认证用户，否者只能读

IsSystemUserOrReadOnly
是后台用户，否则只能读

ReadOnly  HAOHAOXUEXI 好好学习
只能读
"""

from django.contrib.auth import get_user_model
from rest_framework import permissions

from accounts.models import SYSTEM_USER
from accounts.permissions import MY_SAFE_METHODS


class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    # 判断当前用户是否登陆，非登陆用户只能查看
    def has_permission(self, request, view):
        return (
            request.method in MY_SAFE_METHODS or
            request.user and request.user.is_authenticated
        )


class IsSystemUserOrReadOnly(permissions.BasePermission):
    # 只允许后台用户创建、更改、删除，其他用户 和 非登录用户 只能查看
    def has_permission(self, request, view):
        if request.method in MY_SAFE_METHODS:
            return True
        return request.user.type == SYSTEM_USER


class ReadOnly(permissions.BasePermission):
    # 只可以查看
    def has_permission(self, request, view):
        return request.method in MY_SAFE_METHODS
