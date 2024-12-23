from django.contrib import admin
from .models import Weekday, Attendance, HomeWork, User, Science, Room, Diary, Course, Lesson_list, Student_Diary, Message, Student_HomeWork
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Weekday)
admin.site.register(Message)


class StudentDiaryAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "student":
            kwargs["queryset"] = User.objects.filter(type_user="S")  
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Student_Diary, StudentDiaryAdmin)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'science']
    list_filter = ['science']


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'first_name', 'last_name', 'email', 'type_user', 'age'] 
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'age', 'type_user')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'age', 'course'),
        }),
    )
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)


class ScienceAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            kwargs["queryset"] = User.objects.filter(type_user="T")  
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Science, ScienceAdmin)


class AttendanceAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "student":
            kwargs["queryset"] = User.objects.filter(type_user="S")  
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Attendance, AttendanceAdmin)


class DiaryAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "student_diary":
            kwargs["queryset"] = Student_Diary.objects.filter(student__type_user="S")  
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Diary, DiaryAdmin)


class HomeWorkAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            kwargs["queryset"] = User.objects.filter(type_user="T")  
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(HomeWork, HomeWorkAdmin)


class CourseAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            kwargs["queryset"] = User.objects.filter(type_user="T")  
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "students":
            kwargs["queryset"] = User.objects.filter(type_user="S")
        return super().formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(Course, CourseAdmin)


class LessonListAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            kwargs["queryset"] = User.objects.filter(type_user="T")  
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Lesson_list, LessonListAdmin)


class StudentHomeWorkAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "student":
            kwargs["queryset"] = User.objects.filter(type_user="S")  
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Student_HomeWork, StudentHomeWorkAdmin)
