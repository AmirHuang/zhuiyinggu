from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .permissions import IsSystemUserOrReadOnly, IsAuthenticatedOrReadOnly, ReadOnly
from .models import Game, Movie, Music, Book, Video
from .serializers import GameSerializer, MovieSerializer, MusicSerializer, BookSerializer, VideoSerializer


class GameViewset(viewsets.ModelViewSet):
    """
    用于进行 game管理。
    对应 Game 模型，通过过滤器对不同的软件提供不同的接口。
    提供返回某一apk的版本，或者返回某一apk的最新版本。
    只有systemuser可以增加、修改、删除apk版本信息。
    其他普通用户和未登录用户只有查看权限。
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsSystemUserOrReadOnly)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',)
    ordering_fields = ('name',)
    ordering = ('name')
    search_fields = ('name',)

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class MovieViewset(viewsets.ModelViewSet):
    """
    用于进行 game管理。
    对应 Game 模型，通过过滤器对不同的软件提供不同的接口。
    提供返回某一apk的版本，或者返回某一apk的最新版本。
    只有systemuser可以增加、修改、删除apk版本信息。
    其他普通用户和未登录用户只有查看权限。
    """
    queryset = Movie.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsSystemUserOrReadOnly)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',)
    ordering_fields = ('name',)
    ordering = ('name')
    search_fields = ('name',)

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class MusicViewset(viewsets.ModelViewSet):
    """
    用于进行 game管理。
    对应 Game 模型，通过过滤器对不同的软件提供不同的接口。
    提供返回某一apk的版本，或者返回某一apk的最新版本。
    只有systemuser可以增加、修改、删除apk版本信息。
    其他普通用户和未登录用户只有查看权限。
    """
    queryset = Music.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsSystemUserOrReadOnly)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',)
    ordering_fields = ('name',)
    ordering = ('name')
    search_fields = ('name',)

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class BookViewset(viewsets.ModelViewSet):
    """
    用于进行 game管理。
    对应 Game 模型，通过过滤器对不同的软件提供不同的接口。
    提供返回某一apk的版本，或者返回某一apk的最新版本。
    只有systemuser可以增加、修改、删除apk版本信息。
    其他普通用户和未登录用户只有查看权限。
    """
    queryset = Book.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsSystemUserOrReadOnly)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',)
    ordering_fields = ('name',)
    ordering = ('name')
    search_fields = ('name',)

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class VideoViewset(viewsets.ModelViewSet):
    """
    用于进行 game管理。
    对应 Game 模型，通过过滤器对不同的软件提供不同的接口。
    提供返回某一apk的版本，或者返回某一apk的最新版本。
    只有systemuser可以增加、修改、删除apk版本信息。
    其他普通用户和未登录用户只有查看权限。
    """
    queryset = Video.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsSystemUserOrReadOnly)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',)
    ordering_fields = ('name',)
    ordering = ('name')
    search_fields = ('name',)

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)