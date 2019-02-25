"""zhuiyinggu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import xadmin
from django.contrib import admin
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from accounts.views import UserViewset, SystemUserProfileViewSet, UserProfileViewset
from blog.views import BlogViewset
from apk_manage.views import ApkVersionViewSet
from data_manage.views import GameViewset, MovieViewset, MusicViewset
from data_manage.views import VideoViewset, BookViewset
router = DefaultRouter()

# 配置goods的url
router.register(r'users', UserViewset, base_name='users')

router.register(r'sysusers', SystemUserProfileViewSet, base_name='sysusers')

router.register(r'userprofile', UserProfileViewset, base_name='userprofile')

router.register(r'apk', ApkVersionViewSet, base_name='apk')

router.register(r'blog', BlogViewset, base_name='blog')

router.register(r'game', GameViewset, base_name='game')

router.register(r'movie', MovieViewset, base_name='movie')

router.register(r'music', MusicViewset, base_name='music')

router.register(r'video', VideoViewset, base_name='video')

router.register(r'book', BookViewset, base_name='book')

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    re_path('^', include(router.urls)),

    # drf文档, title自定义
    path('docs', include_docs_urls(title='Amir')),

    # drf 入口
    path('api-auth', include('rest_framework.urls')),

    # token
    path('api-token-auth/', views.obtain_auth_token),

    # jwt的token认证接口
    path('login/', obtain_jwt_token),

    # account urls
    path('account/', include('accounts.urls')),
]
