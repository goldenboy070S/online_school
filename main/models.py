from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser


class Auto_timeCreated(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Weekday(Auto_timeCreated):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Room(Auto_timeCreated):
    name = models.CharField(max_length=150)
    science = models.ForeignKey("Science", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    USER_CHOICES = (("T", "Teacher"), ("S", "Student"), ("E", "Employee"))
    type_user = models.CharField(max_length=100, choices=USER_CHOICES, blank=False, null=False)
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Science(Auto_timeCreated):
    name = models.CharField(max_length=150)
    teacher = models.ForeignKey(User, related_name="teachers_science", on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Course(Auto_timeCreated):
    name = models.CharField(max_length=255)
    teacher = models.OneToOneField(User, related_name="teacher_course", on_delete=models.SET_NULL, blank=True, null=True)
    students = models.ManyToManyField(User, related_name="student_course")

    def __str__(self):
        return self.name


class Student_Diary(Auto_timeCreated):
    student = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} kundaligi"


class Message(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.title


class HomeWork(Auto_timeCreated):
    science = models.ForeignKey(Science, on_delete=models.PROTECT)
    title = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    deadline = models.ForeignKey(Weekday, on_delete=models.PROTECT)
    teacher = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Student_HomeWork(Auto_timeCreated):
    home_work = models.ForeignKey(HomeWork, on_delete=models.CASCADE)
    task = models.FileField(upload_to="home_works")
    description = models.TextField()

    def __str__(self):
        return f"{self.home_work.title} uchun" 


class Diary(Auto_timeCreated):
    WORK_TYPE = (("imtihon", "Exam"), ("uy vazifa", "Home work"))
    task_type = models.CharField(max_length=100, choices=WORK_TYPE)
    student_diary = models.ForeignKey(Student_Diary, on_delete=models.CASCADE, related_name="diary")
    home_work = models.ForeignKey(Student_HomeWork, on_delete=models.PROTECT)
    ball = models.PositiveIntegerField(default=0, null=True, blank=True, help_text="0-dan 100-gacha")
    description = models.TextField()

    def clean(self):
        if not (0 <= self.ball <= 100):
            raise ValidationError("Ball qiymati 0 dan 100 gacha bo‘lishi kerak.")

    def __str__(self):
        return f"{self.ball} - {self.description}"


class Attendance(Auto_timeCreated):
    YOQLAMA = (
        ("keldi", "Present"),
        ("kelmadi", "Absent"),
        ("kech", "Late"),
        ("sababli kelmadi", "Reasonably"),
    )

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.ForeignKey(Weekday, on_delete=models.PROTECT)
    status = models.CharField(max_length=100, choices=YOQLAMA)

    def __str__(self):
        return f"{self.course.name} - {self.student.first_name} - {self.status}"


class Lesson_list(Auto_timeCreated):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day = models.ForeignKey(Weekday, on_delete=models.PROTECT)
    science = models.ManyToManyField(Science)

    def __str__(self):
        sciences = ", ".join(science.name for science in self.science.all())
        return f"{self.day.name} | {self.course.name}: {sciences}"
