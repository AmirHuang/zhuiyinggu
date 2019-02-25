"""
apk_manage/views.py

基于Django框架、guardian框架、REST Framework框架，实现RESTful风格接口。

实现ApkVersion模型的 GET LIST POST PUT DELETE 以及自定义相关功能。

支持 用户认证、权限控制、过滤器、限流器、分页。
"""

from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.decorators import list_route
from django_filters.rest_framework import DjangoFilterBackend

from apk_manage.permissions import IsAuthenticatedOrReadOnly
from apk_manage.permissions import IsSystemUserOrReadOnly
from apk_manage.permissions import ReadOnly
from .models import ApkVersion
from .serializers import ApkVersionSerializer


# ApkVersion 版本控制
# ------------------
class ApkVersionViewSet(viewsets.ModelViewSet):
    """
    用于进行 apk的版本控制。
    对应 ApkVersion 模型，通过过滤器对不同的软件提供不同的接口。
    提供返回某一apk的版本，或者返回某一apk的最新版本。
    只有systemuser可以增加、修改、删除apk版本信息。
    其他普通用户和未登录用户只有查看权限。
    """
    queryset = ApkVersion.objects.all()
    serializer_class = ApkVersionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsSystemUserOrReadOnly,)
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter,
                       filters.SearchFilter
                       )
    filter_fields = ('name',)
    ordering_fields = ('name', 'version',)
    ordering = ('name', '-version',)
    search_fields = ('name', 'version',)

    @list_route(methods=['GET'], permission_classes=[ReadOnly], url_path='newest')
    def newest_apk(self, request, *args, **kwargs):
        """
        自定义GET方法，以只读的方式，返回最新的 ApkVersion
        URL: http://www.zhuiyinggu.com:33333/apk/apk_version/newest/
        """
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data[0])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data[0])

    def update(self, request, *args, **kwargs):
        """
        覆写 update()
        设置partial属性为True使其序列化时字段可以部分更新
        """
        partial = True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)