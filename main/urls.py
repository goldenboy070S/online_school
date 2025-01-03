from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import *
router = DefaultRouter()

router.register('weekdays', WeekdayViewSet)
router.register('attendances', AttendanceViewSet)
router.register('homeworks', HomeWorkViewSet)
router.register('student_homework', Student_homeworkViewSet)
router.register('users', UserViewSet, basename="Users")
router.register('science', ScienceViewSet)
router.register('rooms', RoomViewSet)
router.register('diaries', DiaryViewSet)
router.register('courses', CourseViewSet)
router.register('lesson_lists', LessonViewSet)
router.register('student_diary', Student_diaryViewSet)

urlpatterns = router.urls