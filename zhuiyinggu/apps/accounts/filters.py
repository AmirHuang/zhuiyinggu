# _*_ coding: utf-8 _*_
# @Time     : 21:37
# @Author   : Amir
# @Site     : 
# @File     : filters.py
# @Software : PyCharm

import django_filters
from django.contrib.auth import get_user_model
from django_filters.rest_framework import FilterSet
from .models import SystemUserProfile, UserProfile
User = get_user_model()


class UserFilter(FilterSet):

    class Meta:
        model = User
        fields = ['phone', 'email']


class SystemUserProfileFilter(FilterSet):
    username = django_filters.CharFilter(name='user__username')
    email = django_filters.CharFilter(name='user_email')
    phone = django_filters.CharFilter(name='user_phone')

    class Meta:
        model = SystemUserProfile
        # 设置User对象的相关字段，使用 "user" + "__" + "User的相关字段" 的格式。
        fields = ['username', 'email', 'phone', 'nickname']


class UserProfileFilter(FilterSet):
    username = django_filters.CharFilter(name='user__username')
    email = django_filters.CharFilter(name='user_email')
    phone = django_filters.CharFilter(name='user_phone')

    class Meta:
        model = UserProfile
        # 设置User对象的相关字段，使用 "user" + "__" + "User的相关字段" 的格式。
        fields = ['username', 'email', 'phone', 'nickname']


