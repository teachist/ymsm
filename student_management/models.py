from django.db import models


class Area(models.Model):
    """
    行政区划
    """
    name = models.CharField(max_length=100, verbose_name='名称')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL,
                               related_name='subs', null=True, blank=True, verbose_name='上级行政区划')

    class Meta:
        verbose_name = '行政区划'
        verbose_name_plural = '行政区划'

    def __str__(self):
        return self.name


class Student(models.Model):

    name = models.CharField(max_length=12, verbose_name='姓名')
    idno = models.CharField(max_length=18, verbose_name='身份证号码')
    province = models.ForeignKey(
        'Area', on_delete=models.PROTECT, related_name='province_addresses', verbose_name='省')
    city = models.ForeignKey('Area', on_delete=models.PROTECT,
                             related_name='city_addresses', verbose_name='市')
    district = models.ForeignKey(
        'Area', on_delete=models.PROTECT, related_name='district_addresses', verbose_name='区/县')
    country = models.ForeignKey(
        'Area', on_delete=models.PROTECT, related_name='country_addresses', verbose_name='乡镇')

    place = models.CharField(max_length=50, verbose_name='地址')
    mobile = models.CharField(max_length=11, verbose_name='手机')
