"""
accounts/views.py  

基于Django框架、 guardian框架、REST Framework框架，实现 RESTful 风格接口。

提供 User UserProfile SystemUserProfile 模型的 GET LIST POST PUT DELETE 以及自定义相关功能。

支持权限控制、token认证、过滤器、限流器、分页等功能。
"""
from django.contrib.auth import get_user_model

User = get_user_model()

import re
from rest_framework import viewsets, mixins
from rest_framework import filters
from rest_framework.throttling import UserRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.http import HttpResponse
from django.contrib.auth import authenticate

from .models import SystemUserProfile, UserProfile
from .serializers import UserProfileCreateSerializer, UserProfileDetailSerializer
from .serializers import SystemCreateUserProfileSerializer, SystemDetailUserProfileSerializer
from .serializers import UserCreateSerializer, UserDetailSerializer
from .permissions import IsAuthenticatedOrReadOnlyOrCreate
from .permissions import IsOwnerOrReadOnlyOrCreate
from .permissions import IsSystemUserOrOwnerOrReadOnlyOrCreate
from .filters import UserFilter, SystemUserProfileFilter, UserProfileFilter


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # serializer_class = UserSerializer
    permission_classes = (IsSystemUserOrOwnerOrReadOnlyOrCreate,
                          IsAuthenticatedOrReadOnlyOrCreate)
    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication)
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter,
                       filters.SearchFilter)
    # filter_class = UserFilter
    filter_fields = ('phone', 'email')
    ordering_fields = ('email', 'phone')
    search_fields = ('email', 'phone')
    # 设置默认的排序字段
    ordering = ('email',)
    # 按用户限流
    throttle_classes = (UserRateThrottle,)
    # 按作用域限流
    throttle_scope = 'user'

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        baseuser = self.perform_create(serializer)
        re_dict = serializer.data
        payload = jwt_payload_handler(baseuser)
        re_dict['token'] = jwt_encode_handler(payload)
        re_dict['username'] = baseuser.username
        headers = self.get_success_headers(serializer.data)

        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    # def destroy(self, request, *args, **kwargs):
    #     # 覆写 perform_destroy()
    #     # 删除操作为 设置 user 的 is_active 属性为 False
    #     instance = self.get_object()
    #     user = User.objects.get(email=instance.email)
    #     user.is_active = False
    #     user.save()
    #
    #     return Response(user.is_active)

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        else:
            return UserDetailSerializer

    def perform_destroy(self, instance):
        # 覆写 perform_destroy()
        # 删除操作为 设置 user 的 is_active 属性为 False
        user = instance
        user.is_active = False
        user.save()

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

    # @detail_route()
    # def active_user(self, request, pk=None, *args, **kwargs):
    #     # 自定义方法 active_user()
    #     # 实现非活跃用户的激活功能 （设置 is_active 属性为 True）
    #     # URL访问格式为：http://www.zhuiyinggu.com:33333/accounts/users/6/active_user/
    #     # 方法为 GET
    #     instance = self.get_object()
    #     user = User.objects.get(email=instance.email)
    #     user.is_active = True
    #     user.save()
    #     return Response(user.is_active)

    @detail_route()
    def active_user(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = True
        instance.save()
        return Response(instance.is_active)


# 获取所有的SystemUserProfile
class SystemUserProfileViewSet(viewsets.ModelViewSet):
    queryset = SystemUserProfile.objects.all()
    lookup_field = 'nickname'

    permission_classes = (IsAuthenticatedOrReadOnlyOrCreate,
                          IsOwnerOrReadOnlyOrCreate)
    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication)
    # 指定使用 过滤器功能、排序过滤器功能、搜索过滤器功能
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter,
                       filters.SearchFilter)
    filter_class = SystemUserProfileFilter
    ordering_fields = ('nickname', 'user__username', 'user__email', 'user__phone')
    search_fields = ('user__username', 'user__email', 'user__phone', 'nickname')
    # 设置默认的排序字段
    ordering = ('user__email',)

    # 设置限流器
    # 按用户限流
    throttle_classes = (UserRateThrottle,)
    # 按作用域限流
    throttle_scope = 'systemuserprofile'

    def get_serializer_class(self):
        if self.action == 'create':
            return SystemCreateUserProfileSerializer
        else:
            return SystemDetailUserProfileSerializer

    def perform_destroy(self, instance):
        user = instance.user
        user.is_active = False
        user.save()

    @detail_route()
    def active_user(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        user = User.objects.get(email=instance.user.email)
        user.is_active = True
        user.save()
        return Response(user.is_active)

    def update(self, request, *args, **kwargs):
        """
        覆写 update()
        设置partial属性为True使其序列化时字段可以部分更新
        JSON 数据格式如下：
        {
            # 此处为profile的字段
            "user":
            {
                # 此处为user的字段
            }
        }
        """
        partial = True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        payload = jwt_payload_handler(user.user)
        re_dict['token'] = jwt_encode_handler(payload)
        # 在数据 serializer.data中 已经有了nickname 也可以re_dict['username'] = user.user.username
        # re_dict['nickname'] = user.nickname
        headers = self.get_success_headers(serializer.data)

        # print('------------re_dict', re_dict)

        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)


class UserProfileViewset(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    lookup_field = 'nickname'
    permission_classes = (IsAuthenticatedOrReadOnlyOrCreate,
                          IsSystemUserOrOwnerOrReadOnlyOrCreate)
    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = UserProfileFilter
    ordering_fields = ('nickname', 'user__username', 'user__email', 'user__phone')
    # 设置默认的排序字段
    ordering = ('user__email',)
    search_fields = ('nickname', 'user__username', 'user__email', 'user__phone')

    # 设置限流器
    # 按用户限流
    throttle_classes = (UserRateThrottle,)
    # 按作用域限流
    throttle_scope = 'userprofile'

    def get_serializer_class(self):
        if self.action == 'create':
            return UserProfileCreateSerializer
        else:
            return UserProfileDetailSerializer

    # # 方法一：
    # def perform_destroy(self, instance):
    #     user = instance.user
    #     user.is_active = False
    #     user.save()

    # 方法二
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = User.objects.create(email=instance.user.email)
        user.is_active = False
        user.save()

        return Response(user.is_active)

    @detail_route()
    def active_user(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        user = User.objects.get(email=instance.user.email)
        user.is_active = True
        user.save()

        return Response(user.is_active)

    def update(self, request, *args, **kwargs):
        """
        覆写 update()
        设置partial属性为True使其序列化时字段可以部分更新
        JSON 数据格式如下：

        {

            # 此处为profile的字段
            "user":
            {
                # 此处为user的字段
            }
        }

        """
        partial = True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        # 之所以加进去的是user.user 是因为user.user里面才有账号（username）密码（password）
        payload = jwt_payload_handler(user.user)
        re_dict['token'] = jwt_encode_handler(payload)
        re_dict['username'] = user.user.username
        headers = self.get_success_headers(serializer.data)

        print('------------re_dict', re_dict)

        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)


# Token 获取
# ----------
class GetToken(APIView):

    def post(self, request, *args, **kwargs):
        """
        从上传的数据中获取 name 和 password 信息
        判断name的格式，匹配email或者phone或者name
        从数据库中获取指定的User对象
        指定user的验证的用户名为 email，并进行用户验证
        给验证成功的用户设置token，并返回

        token认证，需要在request的头部中包含token信息，格式如下：
        Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
        """
        name = request.data.get('username')

        # 判断name的格式并判断为User的哪一字段
        if re.search('@', name):
            try:
                get_user = User.objects.get(email=name)
            except Exception as e:
                return HttpResponse('user is not exits...')

        elif re.match(r'^[0-9]{11}$', name):
            try:
                get_user = User.objects.get(phone=name)
            except Exception as e:
                return HttpResponse('user is not exits...')
        else:
            try:
                get_user = User.objects.get(username=name)
            except Exception as e:
                return HttpResponse('user is not exits...')

        username = get_user.username
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                token = Token.objects.get_or_create(user=user)
                return Response(token[0].key)
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
