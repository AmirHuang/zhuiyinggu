from datetime import datetime
from django.db import models


class ApkVersion(models.Model):
    name = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    creator = models.CharField(max_length=200)
    create_date = models.DateTimeField(blank=True, default=datetime.now)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '软件管理'
        verbose_name_plural = verbose_name
