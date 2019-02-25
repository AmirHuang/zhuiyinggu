from datetime import datetime
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=200)
    create_date = models.DateTimeField(blank=True, default=datetime.now)
    change_date = models.DateTimeField(blank=True, default=datetime.now)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '博客管理'
        verbose_name_plural = verbose_name