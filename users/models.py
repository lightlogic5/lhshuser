from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

class UserProfile(models.Model):
    employee_id = models.CharField(max_length=100, verbose_name='员工编号')
    password = models.CharField(max_length=100, verbose_name='密码')


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_employee')
    name = models.CharField(max_length=100, verbose_name='姓名', null=True, blank=True)
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    # employee_id = models.CharField(max_length=20, verbose_name='员工编号')
    GENDER_CHOICES = (
        ('male', '男'),
        ('female', '女')
    )
    UNITS_CHOICES = (
        ('ylh','第一联合运行部'),
        ('elh','第二联合运行部')
    )
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES, default='male', verbose_name='性别')
    units = models.CharField(max_length=5, verbose_name='单位', choices=UNITS_CHOICES, null=True, blank=True)
    moblie = models.CharField(max_length=11, verbose_name='手机', null=True, blank=True)
    email = models.CharField(max_length=100, verbose_name='邮箱', null=True, blank=True)
    image = models.ImageField(max_length=100, upload_to='image/%y/%m', default='image/default.png', verbose_name='用户头像')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
