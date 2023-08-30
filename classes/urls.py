from django.urls import path
from classes.views import AddClassroomAPIView, UpdateClassroomAPIView, DeactivateClassroomAPIView, \
    AddTeacherToClassroomAPIView, AddStudentToClassroomAPIView, ListClassroomStudentsAPIView, \
    ListClassroomTeachersAPIView, CreatePost, UpdatePostContentAPIView, DeletePost, LikePost, ListClassroomPosts, \
    ListLikedUsers, CreateComment, ListComments

urlpatterns = [
    path('add-classroom', AddClassroomAPIView.as_view(), name='add-classroom'),
    path('<str:class_id>/update-info/', UpdateClassroomAPIView.as_view(), name='update-info-classroom'),
    path('<str:class_id>/update-info/', UpdateClassroomAPIView.as_view(), name='update-info-classroom'),
    path('<str:class_id>/deactivate/', DeactivateClassroomAPIView.as_view(), name='deactivate-classroom'),
    path('<str:class_id>/add-teachers/', AddTeacherToClassroomAPIView.as_view(), name='add-teacher-join-class'),
    path('<str:class_id>/add-students/', AddStudentToClassroomAPIView.as_view(), name='add-student-join-class'),
    path('<str:class_id>/students/', ListClassroomStudentsAPIView.as_view(), name='list_classroom_students'),
    path('<str:class_id>/teachers/', ListClassroomTeachersAPIView.as_view(), name='list_classroom_teachers'),
    path('<str:class_id>/create-post/', CreatePost.as_view(), name='list_classroom_teachers'),
    path('<str:class_id>/update-post/<str:post_id>/', UpdatePostContentAPIView.as_view(), name='update_post'),
    path('<str:class_id>/delete-post/<str:post_id>/', DeletePost.as_view(), name='delete_post'),
    path('<str:class_id>/like/<str:post_id>/', LikePost.as_view(), name='like_post'),
    path('<str:class_id>/posts/', ListClassroomPosts.as_view(), name='list_classroom_posts'),
    path('<str:class_id>/<str:post_id>/liked-users/', ListLikedUsers.as_view(), name='list_liked_users'),
    path('<str:class_id>/<str:post_id>/create-comment/', CreateComment.as_view(), name='create_comment'),
    path('<str:class_id>/<str:post_id>/comments/', ListComments.as_view(), name='list_comments'),

]
