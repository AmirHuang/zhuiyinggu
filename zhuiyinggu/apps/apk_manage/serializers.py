# _*_ coding: utf-8 _*_
# @Time     : 19:39
# @Author   : Amir
# @Site     : 
# @File     : serializers.py
# @Software : PyCharm

from rest_framework import serializers
from .models import ApkVersion


class ApkVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApkVersion
        fields = '__all__'