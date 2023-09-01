from django.urls import path
from .views import (
    CreateStudentAPIView,
    UpdateStudentByUsernameAPIView,
    ListStudentsAPIView,
    ListStudentsByAdmissionYearAPIView,
    StudentByUsernameAPIView,
    CreateTeacherAPIView,
    UpdateTeacherByUsernameAPIView,
    ListTeachersAPIView,
    TeacherByUsernameAPIView,
    UserLoginAPIView,
    ChangePasswordView, ListUserClassroomsAPIView, ListUserActiveClassroomsAPIView, ListUserInactiveClassroomsAPIView,
)

urlpatterns = [
    path('accounts/login/',UserLoginAPIView.as_view(), name = 'login'),
    path('accounts/change-password/<str:username>/',ChangePasswordView.as_view(), name = 'change-password'),

    path('students/create/', CreateStudentAPIView.as_view(), name='create-student'),
    path('students/get-list-student/', ListStudentsAPIView.as_view(), name='list-students'),
    path('students/get-list-student-by-admission-year/<int:admission_year>/', ListStudentsByAdmissionYearAPIView.as_view(), name='list-students-by-admission-year'),
    path('students/update/<str:username>/', UpdateStudentByUsernameAPIView.as_view(), name='update-student-by-username'),
    path('students/detail/<str:username>/', StudentByUsernameAPIView.as_view(), name='student-by-username'),

    path('teachers/get-list-teacher', ListTeachersAPIView.as_view(), name='list-teachers'),
    path('teachers/update/<str:username>/', UpdateTeacherByUsernameAPIView.as_view(), name='update-teacher-by-username'),
    path('teachers/detail/<str:username>/', TeacherByUsernameAPIView.as_view(), name='teacher-by-username'),
    path('teachers/create/', CreateTeacherAPIView.as_view(), name='create-teacher'),

    path('list-classrooms/', ListUserClassroomsAPIView.as_view(), name='list-user-classrooms'),
    path('list-active-classrooms/', ListUserActiveClassroomsAPIView.as_view(), name='list-user-active-classrooms'),
    path('list-deactive-classrooms/', ListUserInactiveClassroomsAPIView.as_view(),name='list-user-deactivate-classrooms'),

]
