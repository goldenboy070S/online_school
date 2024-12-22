from django.shortcuts import render
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    

class ScienceViewSet(ModelViewSet):
    queryset = Science.objects.all()
    serializer_class = ScienceSerializer


class WeekdayViewSet(ModelViewSet):
    queryset = Weekday.objects.all()
    serializer_class = WeekdaySerializer


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class Student_diaryViewSet(ModelViewSet):
    queryset = Student_Diary.objects.all()
    serializer_class = Student_diarySerializer


class DiaryViewSet(ModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer


class HomeWorkViewSet(ModelViewSet):
    queryset = HomeWork.objects.all()
    serializer_class = HomeWorkSerializer


class LessonViewSet(ModelViewSet):
    queryset = Lesson_list.objects.all()
    serializer_class = LessonSerializer


class AttendanceViewSet(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer




