# _*_ coding: utf-8 _*_
# @Time     : 9:35
# @Author   : Amir
# @Site     : 
# @File     : signals.py
# @Software : PyCharm

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import SYSTEM_USER
User = get_user_model()


# post_save: 接收信号的方式
# sender: 接收信号的model
@receiver(post_save, sender=User)
def create_user(sender, instance=None, created=False, **kwargs):
    # 是否新建, 因为update的时候也会进行post_save
    if created:
        instance.set_password(instance.password)
        instance.is_staff = True
        instance.is_admin = True
        instance.type = SYSTEM_USER
        instance.is_superuser = True
        instance.save()
    # else:
    #     instance.set_password(instance.password)
    #     instance.save()


    # user = instance
    # user.email = validated_data.get('email', user.email)
    # user.name = validated_data.get('name', user.name)
    # user.set_password(validated_data.get('password'))
    # user.phone = validated_data.get('phone', user.phone)
    # user.unid = validated_data.get('unid', user.unid)
    # user.save()
    # return user