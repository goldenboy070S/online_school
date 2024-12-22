from django.contrib import admin
from .models import Weekday, Attendance, HomeWork, Student, Teacher, Science, Room, Diary, Course, Lesson_list, Student_Diary
# Register your models here.
admin.site.register(Weekday)
admin.site.register(Student_Diary)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'science']
    list_filter = ['science']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'mother_name', 'father_name', 'gender', 'course']
    search_fields = ['first_name', 'last_name', 'mother_name', 'father_name']
    list_filter = ['gender', 'age', 'course']


@admin.register(Science)
class ScienceAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher']
    list_filter = ['teacher']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["first_name", 'last_name', 'age']


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['day', 'student', 'status']
    list_filter = ['day', 'status']


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ['task_type', 'home_work', 'description', 'ball', 'student_diary']
    list_filter = ['student_diary']


@admin.register(HomeWork)
class HomeWorkAdmin(admin.ModelAdmin):
    list_display = ['title', 'deadline', 'teacher']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher']


@admin.register(Lesson_list)
class Lesson_listAdmin(admin.ModelAdmin):
    list_display = ['day', 'course']
    list_filter = ['day', 'course']
