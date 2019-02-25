# _*_ coding: utf-8 _*_
# @Time     : 14:39
# @Author   : Amir
# @Site     : 
# @File     : adminx.py
# @Software : PyCharm

import xadmin
from .models import Game, Movie, Music, Book, Video


class GameAdmin(object):
    list_display = ['name', 'description', 'game_type', 'game_step', 'seed_address',
                    'seed_type', 'creator', 'create_date', 'update_date']


class Moviedmin(object):
    list_display = ['name', 'description', 'movie_type', 'movie_step', 'seed_address',
                    'seed_type', 'creator', 'create_date', 'update_date']


class MusicAdmin(object):
    list_display = ['name', 'description', 'singer', 'album', 'music_format',
                    'music_type', 'music_step', 'music_file', 'creator', 'create_date', 'update_date']


class BookAdmin(object):
    list_display = ['name', 'description', 'author', 'book_type', 'book_step',
                    'book_file', 'creator', 'create_date', 'update_date']


class VideoAdmin(object):
    list_display = ['name', 'description', 'video_type', 'video_step', 'seed_address',
                    'seed_type', 'creator', 'create_date', 'update_date']


xadmin.site.register(Game, GameAdmin)
xadmin.site.register(Movie, Moviedmin)
xadmin.site.register(Music, MusicAdmin)
xadmin.site.register(Book, BookAdmin)
xadmin.site.register(Video, VideoAdmin)

