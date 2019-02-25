# _*_ coding: utf-8 _*_
# @Time     : 13:59
# @Author   : Amir
# @Site     : 
# @File     : serializers.py
# @Software : PyCharm

import markdown
from rest_framework import serializers
from blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

    def create(self, validated_data):
        # 覆写create()
        # 创建Blog实例的时候,使用Markdown格式化content文本
        blog = Blog.objects.create(**validated_data)
        blog.content = markdown.markdown(validated_data.get('content', blog.content))
        blog.save()
        return blog

    def update(self, instance, validated_data):
        # 覆写 update()
        # 创建Blog实例的时候,使用Markdown格式化content文本
        blog = instance
        blog.title = validated_data.get('title', blog.title)
        blog.subtitle = validated_data.get('subtitle', blog.subtitle)
        blog.content = markdown.markdown(validated_data.get('content', blog.content))
        blog.change_date = validated_data.get('change_date', blog.change_date)
        blog.address = validated_data.get('address', blog.address)
        # blog.create_date = validated_data.get('create_date', blog.create_date)
        blog.save()
        return blog