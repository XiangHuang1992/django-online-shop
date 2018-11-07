from datetime import datetime

from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    """
    用户
    """
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name='用户名')
    birthday = models.DateField(null=True, blank=True, verbose_name='出生年月')
    mobile = models.CharField(max_length=11, verbose_name='手机号码')
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), verbose_name='性别', default='male')
    email = models.EmailField(max_length=80, null=True, blank=True, verbose_name='邮箱')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class VerifyCode(models.Model):
    code = models.CharField(max_length=10, verbose_name='验证码')
    mobile = models.CharField(max_length=11, verbose_name='手机号码')
    add_time = models.CharField(max_length=25, default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code

