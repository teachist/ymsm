from django.db import models
from users.models import User


class Area(models.Model):
    """
    行政区划
    """
    code = models.CharField(max_length=18, primary_key=True)
    name = models.CharField(max_length=100, verbose_name='名称')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL,
                               related_name='subs', null=True, blank=True, verbose_name='上级行政区划')

    class Meta:
        verbose_name = '行政区划'
        verbose_name_plural = '行政区划'

    def __str__(self):
        return self.name


class ClassGrade(models.Model):
    CLASS_GRADE_CODE = (
        ('0701', '7年级01班'),
        ('0702', '7年级02班'),
        ('0703', '7年级03班'),
        ('0704', '7年级04班'),
        ('0705', '7年级05班'),
        ('0706', '7年级06班'),
        ('0707', '7年级07班'),
        ('0708', '7年级08班'),
        ('0709', '7年级09班'),
        ('0710', '7年级10班'),
        ('0711', '7年级11班'),
        ('0712', '7年级12班'),
    )
    name = models.CharField(
        max_length=4, verbose_name='班级名称', choices=CLASS_GRADE_CODE)
    members = models.IntegerField(verbose_name='人数')

    class Meta:
        verbose_name = '班级'
        verbose_name_plural = '班级'

    def __str__(self):
        return self.get_name_display()


class Student(models.Model):
    user = models.OneToOneField(
        User, verbose_name='姓名', on_delete=models.CASCADE)
    student_id = models.CharField(max_length=19, verbose_name='学籍号')
    is_under_poverty = models.BooleanField(
        default=False, verbose_name='是否精准扶贫')
    is_disability = models.BooleanField(default=False, verbose_name='是否残疾')
    # Area
    class_name = models.ForeignKey(
        ClassGrade, on_delete=models.CASCADE, verbose_name='班级')
    province = models.ForeignKey(
        'Area', limit_choices_to={'parent__isnull': True}, on_delete=models.PROTECT, related_name='province_addresses',
        verbose_name='省')
    city = models.ForeignKey('Area', limit_choices_to={'parent__isnull': False}, on_delete=models.PROTECT,
                             related_name='city_addresses', verbose_name='市')
    district = models.ForeignKey(
        'Area', on_delete=models.PROTECT, related_name='district_addresses', verbose_name='区/县')
    country = models.ForeignKey(
        'Area', on_delete=models.PROTECT, related_name='country_addresses', verbose_name='乡镇')
    address = models.CharField(max_length=100, verbose_name='家庭住址')
    parents_name = models.CharField(verbose_name='监护人', max_length=12)
    contact = models.CharField(max_length=11, verbose_name='联系人电话')

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = '学生'

    def __str__(self):
        return self.user.full_name()

    def get_address(self):
        return f'{self.province}{self.city}{self.district}{self.country}{self.address}'
    get_address.short_description = '家庭住址'

    def birthday(self):
        return f'{self.user.identity_card[6:10]}-{self.user.identity_card[10:12]}-{self.user.identity_card[12:14]}'
    birthday.short_description = '出生日期'
