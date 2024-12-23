from django.shortcuts import render
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.mail import send_mail
from online_school.settings import EMAIL_HOST_USER
from rest_framework.permissions import DjangoModelPermissions, BasePermission
from .models import Message
from rest_framework.permissions import AllowAny
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

class IsAuthenticatedOrPostOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST' and not request.user.is_authenticated or request.user.is_superuser:
            return True
        elif request.method == 'GET' and request.user.is_superuser:
            return True
        return False


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticatedOrPostOnly]  
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def get_queryset(self):
        if self.action == 'list':
            teachers = User.objects.filter(type_user="T")
            students = User.objects.filter(type_user="S")
            return students  
        return super().get_queryset()

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserUpdateSerializer

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class Student_diaryViewSet(ModelViewSet):
    queryset = Student_Diary.objects.all()
    serializer_class = Student_DiarySerializer

    def retrieve(self, request, pk=None):
        queryset = Student_Diary.objects.all()
        category = queryset.get(pk=pk)
        serializer = Student_diaryRetriveSerializer(category)
        return Response(serializer.data)


class DiaryViewSet(ModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer


class HomeWorkViewSet(ModelViewSet):
    queryset = HomeWork.objects.all()
    serializer_class = HomeWorkSerializer


class LessonViewSet(ModelViewSet):
    queryset = Lesson_list.objects.all()
    serializer_class = Lesson_listSerializer


class AttendanceViewSet(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class Student_homeworkViewSet(ModelViewSet):
    queryset = Student_HomeWork.objects.all()
    serializer_class = Student_HomeWorkSerializer


class MessageApiView(APIView):
    permission_classes = []
    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        send_mail(
            subject=serializer.validated_data.get('title'),
            message=serializer.validated_data.get('content'),
            from_email=EMAIL_HOST_USER,
            recipient_list=[student.email for student in User.objects.all() if student.email is not None],
            fail_silently=False,
        )
        Message.objects.create(title=serializer.validated_data.get('title'),
            message=serializer.validated_data.get('content'))
        return Response('Message sent successfully')