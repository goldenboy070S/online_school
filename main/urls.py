from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import *
router = DefaultRouter()

router.register('weekdays', WeekdayViewSet)

router.register('attendances', AttendanceViewSet)

router.register('homeworks', HomeWorkViewSet)

router.register('students', StudentViewSet)

router.register('teachers', TeacherViewSet)

router.register('science', ScienceViewSet)

router.register('rooms', RoomViewSet)

router.register('diaries', DiaryViewSet)

router.register('courses', CourseViewSet)

router.register('lesson_lists', LessonViewSet)

router.register('student_diary', Student_diaryViewSet)

urlpatterns = router.urls