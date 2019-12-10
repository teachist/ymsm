from django.contrib import admin
from .models import ClassGrade, Student, Area
from utils.mixins import ExportCsvMixin


class StudentAdmin(admin.ModelAdmin, ExportCsvMixin):
    actions = ['export_as_csv']
    list_display = ('full_name', 'gender', 'identity_card_number', 'class_name', 'birthday',
                    'get_address', 'parents_name', 'contact', 'is_under_poverty', 'is_disability', )

    def full_name(self, obj):
        return obj.user.full_name()
    full_name.short_description = '姓名'

    def gender(self, obj):
        return obj.user.get_gender_display()
    gender.short_description = '性别'

    def identity_card_number(self, obj):
        return obj.user.identity_card
    identity_card_number.short_description = '身份证号码'


admin.site.register(ClassGrade)
admin.site.register(Student, StudentAdmin)
admin.site.register(Area)
