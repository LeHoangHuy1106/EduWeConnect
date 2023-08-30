import random
import string


from django.contrib.auth.models import User
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.serializers import StudentSerializer, TeacherSerializer, UserSerializer
from .models import Classroom, Post, Comment
from .permissions import CanAddClassroom, CanUpdateInfoClassroom, IsStudentOrTeacherInClass
from .serializers import ClassroomSerializer, PostSerializer, CommentSerializer
from users.models import Student, Teacher

class AddClassroomAPIView(APIView):
    permission_classes = [CanAddClassroom]
    def post(self, request):
        serializer = ClassroomSerializer(data=request.data)
        if serializer.is_valid():
            current_class_count = Classroom.objects.count()
            class_id = f"class{current_class_count + 1:05d}"
            serializer.validated_data['class_id'] = class_id
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateClassroomAPIView(APIView):
    permission_classes = [CanUpdateInfoClassroom]
    def put(self, request, class_id):
        try:
            classroom = Classroom.objects.get(class_id=class_id)
        except Classroom.DoesNotExist:
            return Response({"message": "Classroom not found."}, status=status.HTTP_404_NOT_FOUND)

        info = request.data.get('info')
        if info:
            classroom.info = info
            classroom.save()
            return Response({"message": "Classroom info updated."})
        return Response({"message": "Info field is required."}, status=status.HTTP_400_BAD_REQUEST)

class DeactivateClassroomAPIView(APIView):
    permission_classes = [CanAddClassroom]
    def put(self, request, class_id):
        try:
            classroom = Classroom.objects.get(class_id=class_id)
        except Classroom.DoesNotExist:
            return Response({"message": "Classroom not found."}, status=status.HTTP_404_NOT_FOUND)

        classroom.is_active = False
        classroom.save()
        return Response({"message": "Classroom deactivated."})


class AddTeacherToClassroomAPIView(APIView):
    def post(self, request, class_id):
        try:
            classroom = Classroom.objects.get(class_id=class_id)
        except Classroom.DoesNotExist:
            return Response({"message": "Classroom not found."}, status=status.HTTP_404_NOT_FOUND)

        teacher_username_list = request.data.get('teachers', [])

        for teacher_username in teacher_username_list:
            try:
                user = User.objects.get(username=teacher_username)

                # Kiểm tra xem giáo viên đã được thêm vào lớp học chưa
                if user not in classroom.teachers.all():
                    classroom.teachers.add(user)
                    teacher, created = Teacher.objects.get_or_create(user=user)
                    teacher.class_join.add(classroom)
            except User.DoesNotExist:
                pass

        return Response({"message": "Teachers added to classroom."})

class AddStudentToClassroomAPIView(APIView):
    def post(self, request, class_id):
        try:
            classroom = Classroom.objects.get(class_id=class_id)
        except Classroom.DoesNotExist:
            return Response({"message": "Classroom not found."}, status=status.HTTP_404_NOT_FOUND)

        student_username_list = request.data.get('students', [])

        for student_username in student_username_list:
            try:
                user = User.objects.get(username=student_username)

                # Kiểm tra xem học sinh đã được thêm vào lớp học chưa
                if user not in classroom.students.all():
                    classroom.students.add(user)
                    student, created = Student.objects.get_or_create(user=user)
                    student.class_join.add(classroom)
            except User.DoesNotExist:
                pass
        return Response({"message": "Students added to classroom."})



class ListClassroomStudentsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, class_id):
        try:
            classroom = Classroom.objects.get(class_id=class_id)
        except Classroom.DoesNotExist:
            return Response({"message": "Classroom not found."}, status=status.HTTP_404_NOT_FOUND)

        students = classroom.students.all()
        serialized_students = StudentSerializer(students, many=True)  # Tùy chỉnh Serializer cho Student
        return Response(serialized_students.data)


class ListClassroomsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        classrooms = Classroom.objects.all()
        serializer = ClassroomSerializer(classrooms, many=True)
        return Response(serializer.data)


class ListClassroomStudentsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, class_id):
        try:
            classroom = Classroom.objects.get(class_id=class_id)
        except Classroom.DoesNotExist:
            return Response({"message": "Classroom not found."}, status=status.HTTP_404_NOT_FOUND)

        students = classroom.students.all()
        serialized_students = UserSerializer(students, many=True)
        return Response(serialized_students.data)

class ListClassroomTeachersAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, class_id):
        try:
            classroom = Classroom.objects.get(class_id=class_id)
        except Classroom.DoesNotExist:
            return Response({"message": "Classroom not found."}, status=status.HTTP_404_NOT_FOUND)

        teachers = classroom.teachers.all()
        serialized_teachers = UserSerializer(teachers, many=True)
        return Response(serialized_teachers.data)



class CreatePost(APIView):
    permission_classes = [IsStudentOrTeacherInClass]

    def post(self, request, class_id):
        try:
            classroom = Classroom.objects.get(class_id=class_id)
        except Classroom.DoesNotExist:
            return Response({"message": "Classroom not found."}, status=status.HTTP_404_NOT_FOUND)
        classroom = Classroom.objects.get(class_id=class_id)
        post_count = classroom.posts.count()
        next_post_number = post_count + 1
        post_id = f"post{class_id}{next_post_number:05}"
        post_data = {
            "post_id" : post_id,
            "classroom": classroom.class_id,
            "author": request.user.id,
            "content": request.data.get("content"),
            "is_edited": False
        }

        serializer = PostSerializer(data=post_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdatePostContentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, class_id, post_id):
        try:
            post = Post.objects.get(post_id=post_id, classroom__class_id=class_id)
        except Post.DoesNotExist:
            return Response({"message": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

        if post.author != request.user:
            return Response({"message": "You don't have permission to edit this post."}, status=status.HTTP_403_FORBIDDEN)

        content = request.data.get("content")
        if content is None:
            return Response({"message": "Content field is required."}, status=status.HTTP_400_BAD_REQUEST)

        post.content = content
        post.is_edited = True
        post.save()

        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeletePost(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, class_id, post_id):
        post = get_object_or_404(Post, post_id=post_id, classroom__class_id=class_id)

        if post.author != request.user:
            return Response({"message": "You don't have permission to delete this post."},
                            status=status.HTTP_403_FORBIDDEN)
        post.delete()
        return Response({"message": "Post deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

class LikePost(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, class_id, post_id):
        post = get_object_or_404(Post, post_id=post_id, classroom__class_id=class_id)

        if request.user.is_superuser or (request.user in post.classroom.teachers.all()) or (request.user in post.classroom.students.all()):
            if request.user in post.likes.all():
                post.likes.remove(request.user)
                return Response({"message": "Post unliked successfully."}, status=status.HTTP_200_OK)
            else:
                post.likes.add(request.user)
                return Response({"message": "Post liked successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "You don't have permission to like this post."},
                            status=status.HTTP_403_FORBIDDEN)


class ListClassroomPosts(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, class_id):
        classroom = get_object_or_404(Classroom, class_id=class_id)

        if request.user.is_superuser or (request.user in classroom.teachers.all()) or (
                request.user in classroom.students.all()):
            posts = Post.objects.filter(classroom=classroom)
            post_data = []
            for post in posts:
                post_info = {
                    "post_id": post.post_id,
                    "content": post.content,
                    "author": post.author.username,
                    "created_date": post.created_date,
                    "likes": post.likes.count(),
                    "is_edited": post.is_edited
                }
                post_data.append(post_info)
            return Response(post_data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "You don't have permission to access posts in this classroom."},
                            status=status.HTTP_403_FORBIDDEN)

class ListLikedUsers(APIView):
    def get(self, request, class_id, post_id):
        classroom = get_object_or_404(Classroom, class_id=class_id)
        post = get_object_or_404(Post, post_id=post_id, classroom=classroom)

        if request.user.is_superuser or (request.user in classroom.teachers.all()) or (request.user in classroom.students.all()):
            liked_users = post.likes.all()
            liked_users_list = [f"{user.first_name} {user.last_name} ({user.username})" for user in liked_users]
            return Response(liked_users_list, status=status.HTTP_200_OK)
        else:
            return Response({"message": "You do not have permission to access this information."}, status=status.HTTP_403_FORBIDDEN)


class CreateComment(APIView):
    def post(self, request, class_id, post_id):
        classroom = get_object_or_404(Classroom, class_id=class_id)
        post = get_object_or_404(Post, post_id=post_id, classroom=classroom)

        if request.user.is_superuser or (request.user in classroom.teachers.all()) or (
                request.user in classroom.students.all()):
            comment_id = "cmt" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
            comment_data = {
                "comment_id": comment_id,
                "content": request.data.get("content"),
                "author": request.user,
                "post": post
            }
            comment = Comment(**comment_data)
            comment.save()
            comment_serializer = CommentSerializer(comment)
            return Response(comment_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "You do not have permission to create a comment for this post."},
                            status=status.HTTP_403_FORBIDDEN)


class ListComments(APIView):
    def get(self, request, class_id, post_id):
        classroom = get_object_or_404(Classroom, class_id=class_id)
        post = get_object_or_404(Post, post_id=post_id, classroom=classroom)

        if request.user.is_superuser or (request.user in classroom.teachers.all()) or (
                request.user in classroom.students.all()):
            comments = Comment.objects.filter(post=post)
            comment_serializer = CommentSerializer(comments, many=True)
            return Response(comment_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "You do not have permission to view comments for this post."},
                            status=status.HTTP_403_FORBIDDEN)