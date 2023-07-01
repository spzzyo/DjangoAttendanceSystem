from django.contrib import admin

# Register your models here.
from .models import *
from django.contrib.auth.admin import UserAdmin

class UserModel(UserAdmin):
    list_display=['username', 'user_type']

admin.site.register(CustomUser, UserModel)
admin.site.register(Course)
admin.site.register(Session_Year)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(Staff_Notifaction)
admin.site.register(Staff_Leave)
admin.site.register(Staff_Feedback)
admin.site.register(Student_Notifaction)
admin.site.register(Student_Leave)
admin.site.register(Attendance)
admin.site.register(Attendance_Report)
admin.site.register(Student_Result)
