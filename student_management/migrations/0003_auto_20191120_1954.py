# Generated by Django 2.2.7 on 2019-11-20 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management', '0002_remove_student_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='country',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='country_addresses', to='student_management.Area', verbose_name='乡镇'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='mobile',
            field=models.CharField(default='', max_length=11, verbose_name='手机'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='district_addresses', to='student_management.Area', verbose_name='区/县'),
        ),
        migrations.AlterField(
            model_name='student',
            name='idno',
            field=models.CharField(max_length=18, verbose_name='身份证号码'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=12, verbose_name='姓名'),
        ),
    ]
