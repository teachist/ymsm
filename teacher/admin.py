from django.contrib import admin
from .models import Courses, Teacher, LeaderTeacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'major', 'teacher_in_classes',
                    'teacher_phonenumber', )

    def teacher_in_classes(self, obj):
        classes = []
        for tem_class in obj.teach_classes.all():
                classes.append(tem_class.get_name_display())
                return ','.join(classes)
    teacher_in_classes.short_description = '所教班级'

    def teacher_phonenumber(self, obj):
        return obj.user.telphone


admin.site.register(Courses)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(LeaderTeacher)
