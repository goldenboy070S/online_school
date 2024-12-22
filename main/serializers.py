from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Weekday, Attendance, HomeWork, Student, Teacher, Science, Room, Diary, Course, Lesson_list, Student_Diary

class WeekdaySerializer(ModelSerializer):
    class Meta:
        model = Weekday
        fields = '__all__'
        read_only = ['id']


class AttendanceSerializer(ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
        read_only = ['id']
        depth = 1


class HomeWorkSerializer(ModelSerializer):
    class Meta:
        model = HomeWork
        fields = '__all__'
        read_only = ['id']
        depth = 1


class Student_diarySerializer(ModelSerializer):
    class Meta:
        model = Student_Diary
        fields = '__all__'
        read_only = ['id']


class StudentSerializer(ModelSerializer):
    diary = Student_diarySerializer(read_only=True)

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'mother_name', 'father_name', 'gender', 'course', 'diary']
        read_only = ['id']
        depth = 1


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        read_only = ['id']
        depth = 1


class ScienceSerializer(ModelSerializer):
    class Meta:
        model = Science
        fields = '__all__'
        read_only = ['id']
        depth = 1


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        read_only = ['id']


class DiarySerializer(ModelSerializer):
    class Meta:
        model = Diary
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson_list
        fields = '__all__'


















