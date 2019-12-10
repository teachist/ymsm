from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    GENDERS = (
        (0, '男'),
        (1, '女')
    )
    image = models.ImageField(verbose_name='相片', max_length=200,
                              blank=True, null=True, upload_to='users/avatars')
    identity_card = models.CharField(max_length=18, verbose_name='身份证')
    telphone = models.CharField(max_length=11, verbose_name='电话号码')
    gender = models.IntegerField(verbose_name='性别', choices=GENDERS)

    is_student = models.BooleanField(verbose_name='学生')
    is_teacher = models.BooleanField(verbose_name='教师')
    is_chef_teacher = models.BooleanField(verbose_name='班主任')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return self.last_name + self.first_name
    full_name.short_description = '姓名'
