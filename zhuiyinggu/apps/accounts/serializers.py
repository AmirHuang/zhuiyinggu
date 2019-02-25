# _*_ coding: utf-8 _*_
# @Time     : 17:14
# @Author   : Amir
# @Site     : 
# @File     : serializers.py
# @Software : PyCharm

import re
from django.contrib.auth import get_user_model

User = get_user_model()

from zhuiyinggu.settings import REGEX_MOBILE
from rest_framework import serializers
from accounts.models import SystemUserProfile, UserProfile, SYSTEM_USER, COMMON_USER


# User 序列化器
class UserCreateSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='user-detail', lookup_field='pk')
    password = serializers.CharField(style={'input_type': 'password'},
                                     label='密码', write_only=True)
    phone = serializers.CharField(max_length=11)

    def validate_phone(self, phone):
        if not re.match(REGEX_MOBILE, phone):
            raise serializers.ValidationError('手机号码非法！')
        else:
            return phone

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'phone', 'unid')

    # def create(self, validated_data):
    #     # 覆盖create（）
    #     # 创建User实例的时候设置密码，并增加相应权限
    #     user = User.objects.create(**validated_data)
    #     # 修改密码：将python字符串使用MD5加密
    #     user.set_password(validated_data.pop('password'))
    #     user.is_admin = True
    #     user.is_superuser = True
    #     user.save()
    #     return user


class UserDetailSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=11)

    def validate_phone(self, phone):
        if not re.match(REGEX_MOBILE, phone):
            raise serializers.ValidationError('手机号码非法！')
        else:
            return phone

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone', 'unid')

    # def update(self, instance, validated_data):
    #     # 覆盖update（）
    #     # 同时可以更新User实例的信息
    #     user = instance
    #     # user.email = validated_data.get('email', user.email)
    #     user.username = validated_data.get('username', user.username)
    #     # user.set_password(validated_data.get('password'))
    #     user.phone = validated_data.get('phone', user.phone)
    #     user.unid = validated_data.get('unid', user.unid)
    #     user.save()
    #     return user


# SystemUserProfile 序列器
class SystemCreateUserProfileSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='systemuserprofile',
    #                                            lookup_field='nickname')
    # 嵌套UserSerializer（）序列器
    user = UserCreateSerializer(required=False)

    class Meta:
        model = SystemUserProfile
        fields = ('id', 'nickname', 'date_of_birth', 'user')

    def create(self, validated_data):
        # 覆盖create（）
        # 创建SystemUserProfile实例的同时 创建一个User实例，
        # 并给User实例设置一个密码和增加相应的权限
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        user.set_password(user_data.pop('password'))
        # 给创建的用户分配admin权限
        user.is_admin = True
        # 给创建的用户分配superuser权限
        user.is_superuser = True
        user.type = SYSTEM_USER
        user.save()
        systemuserprofile = SystemUserProfile.objects.create(user=user, **validated_data)
        return systemuserprofile


# SystemUserProfile 序列器
class SystemDetailUserProfileSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='systemuserprofile',
    #                                            lookup_field='nickname')
    # 嵌套UserSerializer（）序列器
    user = UserDetailSerializer(required=False)

    class Meta:
        model = SystemUserProfile
        fields = ('id', 'nickname', 'date_of_birth', 'user')

    def update(self, instance, validated_data):
        # 覆盖 update（）
        # 同时可以更新SystemUserProfile实例和User实例的信息
        user_data = validated_data.pop('user')
        user = instance.user
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.save()

        user.email = user_data.get('email', user.email)
        user.username = user_data.get('username', user.username)
        # user.set_password(user_data.get('password'))
        user.phone = user_data.get('phone', user.phone)
        user.unid = user_data.get('unid', user.unid)
        user.save()
        return instance


# UserProfile 序列化器
class UserProfileCreateSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='userprofile-detail', lookup_field='nickname')
    user = UserCreateSerializer(required=False)

    class Meta:
        model = UserProfile
        fields = ('nickname', 'date_of_birth', 'user')

    def create(self, validated_data):
        # 覆盖create（）
        # 创建UserProfile实例的同时 创建一个User实例，
        # 并给User实例设置一个密码和增加相应的权限
        user_data = validated_data.pop('user')
        print('------------validated_data', validated_data)
        user = User.objects.create(**user_data)
        user.set_password(user_data.pop('password'))
        user.type = COMMON_USER
        user.save()

        userprofile = UserProfile.objects.create(user=user, **validated_data)
        return userprofile


# UserProfile 序列化器
class UserProfileDetailSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='userprofile-detail', lookup_field='nickname')
    user = UserDetailSerializer(required=False)

    class Meta:
        model = UserProfile
        fields = ('nickname', 'date_of_birth', 'user')

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user

        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.save()

        user.email = user_data.get('email', user.email)
        user.username = user_data.get('username', user.username)
        # user.set_password(user_data.get('password'))
        user.phone = user_data.get('phone', user.phone)
        user.unid = user_data.get('unid', user.unid)
        user.save()

        return instance
