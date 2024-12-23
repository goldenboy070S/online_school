from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Weekday, Attendance, HomeWork, User, Science, Room, Diary, Course, Lesson_list, Student_Diary, Student_HomeWork
from django.core.validators import EmailValidator
from django.contrib.auth.models import Group

class WeekdaySerializer(ModelSerializer):
    class Meta:
        model = Weekday
        fields = '__all__'
        read_only = ['id']


class AttendanceSerializer(serializers.ModelSerializer):
  
    student = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(type_user="S"))

    class Meta:
        model = Attendance
        fields = ['id', 'course', 'student', 'day', 'status']


class HomeWorkSerializer(serializers.ModelSerializer):
   
    teacher = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(type_user="T"))

    class Meta:
        model = HomeWork
        fields = ['id', 'science', 'title', 'course', 'deadline', 'teacher']


class DiarySerializer(serializers.ModelSerializer):
    
    student_diary = serializers.PrimaryKeyRelatedField(queryset=Student_Diary.objects.filter(student__type_user="S"))

    class Meta:
        model = Diary
        fields = ['id', 'task_type', 'student_diary', 'home_work', 'ball', 'description']


class Student_diaryRetriveSerializer(ModelSerializer):
    diary = DiarySerializer(read_only=True, many=True)

    class Meta:
        model = Student_Diary
        fields = ['student', 'diary']
        read_only = ['id']
        depth = 1


class Student_DiarySerializer(serializers.ModelSerializer):

    student = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(type_user="S"))

    class Meta:
        model = Student_Diary
        fields = ['id', 'student']


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['type_user', 'first_name', 'last_name', 'age', 'email']

    def validate_age(self, value):
        if value < 20 or value > 100:
            raise serializers.ValidationError("Yosh chegarasi 20 dan 100 gacha bo'lishi kerak.")
        return value



class UserCreateSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirmation']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class ScienceSerializer(ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(type_user="T"))

    class Meta:
        model = Science
        fields = ['name', 'teacher']
        read_only = ['id']
        depth = 1


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        read_only = ['id']


class CourseSerializer(serializers.ModelSerializer):
    
    students = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(type_user="S"),
        many=True
    )
    
    teacher = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(type_user="T"),
        required=False
    )

    class Meta:
        model = Course
        fields = ['id', 'name', 'teacher', 'students']



class Lesson_listSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson_list
        fields = ['id', 'course', 'day', 'science']



class MessageSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    content = serializers.CharField()
    

class Student_HomeWorkSerializer(serializers.ModelSerializer):
    
    home_work = serializers.PrimaryKeyRelatedField(queryset=HomeWork.objects.filter(teacher__type_user="T"))

    class Meta:
        model = Student_HomeWork
        fields = ['id', 'home_work', 'task', 'description']















