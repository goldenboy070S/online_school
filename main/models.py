from django.db import models
from django.core.exceptions import ValidationError


class Auto_timeCreated(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Weekday(Auto_timeCreated):
    """Hafta Kunlari"""
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    

class Room(Auto_timeCreated):
    """Xonalar"""
    name = models.CharField(max_length=150)
    science = models.ForeignKey("Science", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Teacher(Auto_timeCreated):
    """O'qituvchilar"""
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.PositiveIntegerField()

    def clean(self):
        if self.age < 20 or self.age > 100:
            raise ValidationError("yosh chegarasi 20 dan 100 gacha bo‘lishi kerak.")
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Science(Auto_timeCreated):
    """Fanlar"""
    name = models.CharField(max_length=150)
    teacher = models.ForeignKey(Teacher, related_name="teachers_science", on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Course(Auto_timeCreated):
    """Sinflar"""
    name = models.CharField(max_length=255)
    teacher = models.OneToOneField(Teacher, related_name="teacher_course", on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Student(Auto_timeCreated):
    """O'quvchilar"""
    GENDER_CHOICES = (("M", "Male"), ("F", "Female"))
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    mother_name = models.CharField(max_length=150)
    father_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    course = models.ForeignKey(Course, related_name="students_course", on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student_Diary(Auto_timeCreated):
    """Oquvchi kundaligi"""
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} kundaligi"


class HomeWork(Auto_timeCreated):
    science = models.ForeignKey(Science, on_delete=models.PROTECT)
    title = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    deadline = models.ForeignKey(Weekday, on_delete=models.PROTECT)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Diary(Auto_timeCreated):
    """Kundalikni baholash"""
    WORK_TYPE = (('imtihon', "Exam"), ('uy vazifa', "Home work"))
    task_type = models.CharField(max_length=100, choices=WORK_TYPE)
    student_diary = models.ForeignKey(Student_Diary, on_delete=models.CASCADE, related_name="diary")
    home_work = models.ForeignKey(HomeWork, on_delete=models.PROTECT)
    ball = models.PositiveIntegerField(default=0, null=True, blank=True, help_text="0-dan 100-gacha")
    description = models.CharField(max_length=1000)

    def clean(self):
        if self.ball < 0 or self.ball > 100:
            raise ValidationError("Ball qiymati 0 dan 100 gacha bo‘lishi kerak.")

    def __str__(self):
        return f"{self.ball} - {self.description}"


class Attendance(Auto_timeCreated):
    YOQLAMA = (('keldi', "Present"), ('kelmadi', "Absent"), ('kech', "Late"), ('sababli kelmadi', "Reasonably"))
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    day = models.ForeignKey(Weekday, on_delete=models.PROTECT)
    status = models.CharField(max_length=100, choices=YOQLAMA)


class Lesson_list(Auto_timeCreated):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day = models.ForeignKey(Weekday, on_delete=models.PROTECT)
    Science = models.ManyToManyField(Science) 

    def __str__(self):
        return f"{self.day.name}_{self.course.name} | {self.Science.name}"

BARCHA_CLASSLAR = [Weekday, Attendance, HomeWork, Student, Teacher, Science, Room, Diary, Course]