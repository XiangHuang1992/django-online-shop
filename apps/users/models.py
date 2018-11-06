from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    """
    用户
    """
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name='用户名')
    birthday = models.DateField(null=True, blank=True, verbose_name='出生年月')
    mobile = models.CharField()
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), verbose_name='性别')
    email = models.EmailField(max_length=80, null=True, blank=True, verbose_name='邮箱')