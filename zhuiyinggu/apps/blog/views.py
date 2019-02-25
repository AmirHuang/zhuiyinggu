from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import viewsets, mixins, filters
from rest_framework.decorators import list_route
from django_filters.rest_framework import DjangoFilterBackend
from blog.models import Blog
from blog.serializers import BlogSerializer
from blog.permissions import IsAuthenticatedOrReadOnly, IsSystemUserOrReadOnly, ReadOnly
User = get_user_model()


class BlogViewset(viewsets.ModelViewSet):

    def get_queryset(self):
        newest = self.request.GET.get('newest')
        if newest == 'newest':
            return Blog.objects.all().order_by('-create_date').first()
        else:
            return Blog.objects.all()

    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsSystemUserOrReadOnly)
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter,
                       filters.SearchFilter)
    filter_fields = ('title',)
    ordering_fields = ('title', 'subtitle', 'author',)
    ordering = ('title',)
    search_fields = ('title', 'author',)

    @list_route(methods=['GET'], permission_classes=[ReadOnly], url_path='newest')
    def newest_blog(self, request, *args, **kwargs):
        """
        自定义GET方法，以只读的方式，返回最新的 Blog
        URL: http://www.zhuiyinggu.com:33333/blog/blog/newest/
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
