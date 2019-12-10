from django.db import models
from users.models import User
from student_management.models import ClassGrade


class Courses(models.Model):
    title = models.CharField(max_length=10, verbose_name='课程名')

    def __str__(self):
        return self.title


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    major = models.CharField(verbose_name='专业', max_length=20)
    description = models.CharField(max_length=200, verbose_name='简介', blank=True, null=True)
    teach_classes = models.ManyToManyField(ClassGrade)
    teach_courses = models.ManyToManyField(Courses)

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = '教师'

    def __str__(self):
        return self.user.full_name()


class LeaderTeacher(models.Model):
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    manage_class = models.ForeignKey(ClassGrade, on_delete=models.SET_NULL, verbose_name='负责班级', null=True)

    class Meta:
        verbose_name = '班主任'
        verbose_name_plural = '班主任'

    def __str__(self):
        return self.teacher.user.full_name()


