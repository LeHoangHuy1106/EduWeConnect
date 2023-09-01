from django.contrib.auth.hashers import check_password

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import update_session_auth_hash

from classes.models import Classroom
from classes.serializers import ClassroomSerializer
from .helpers import create_teacher_account, create_student_account
from .models import Student, Teacher
from .serializers import StudentSerializer, TeacherSerializer
from .permissions import CanUpdateProfile, CanViewStudentList, CanViewStudentDetail, CanAddStudentAndTeacher
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication

#============================ Student API ============================#
class CreateStudentAPIView(APIView):
    permission_classes = [CanAddStudentAndTeacher]

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            admission_year = serializer.validated_data.get('admission_year')
            current_student_count = Student.objects.filter(admission_year=admission_year).count()
            serializer.validated_data['isFirstLogin'] = True
            serializer.validated_data['user']['username'] = f"hs{admission_year}{current_student_count + 1:04}"
            serializer.validated_data['user']['password'] = serializer.validated_data['phone_number']
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateStudentByUsernameAPIView(APIView):
    permission_classes = [CanViewStudentDetail]
    def put(self, request, username):
        student = Student.objects.get(user__username=username)

        if request.user != student.user:
            return Response({"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ListStudentsAPIView(APIView):
    permission_classes = [CanViewStudentList]
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
class ListStudentsByAdmissionYearAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Chỉ admin mới có quyền

    def get(self, request, admission_year):
        students = Student.objects.filter(admission_year=admission_year)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
class StudentByUsernameAPIView(APIView):
    permission_classes = [IsAuthenticated, CanUpdateProfile]

    def get(self, request, username):
        student = Student.objects.get(user__username=username)

        if request.user != student.user and not request.user.is_staff:
            return Response({"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = StudentSerializer(student)
        return Response(serializer.data)
#============================ Teacher API ============================#
class CreateTeacherAPIView(APIView):
    permission_classes = [CanAddStudentAndTeacher]
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            current_teacher_count = Teacher.objects.count()
            hire_date = serializer.validated_data.get('hire_date')
            if hire_date:
                graduation_year = hire_date.year  # Lấy năm từ hire_date
            else:
                graduation_year = None

            serializer.validated_data['isFirstLogin'] = True
            serializer.validated_data['user']['password'] = serializer.validated_data['phone_number']
            serializer.validated_data['user']['username'] = f"gv{graduation_year}{current_teacher_count + 1:04}"
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateTeacherByUsernameAPIView(APIView):
    permission_classes = [IsAuthenticated, CanUpdateProfile]

    def put(self, request, username):
        teacher = Teacher.objects.get(user__username=username)

        if request.user != teacher.user:
            return Response({"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = TeacherSerializer(teacher, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ListTeachersAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Chỉ admin mới có quyền

    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
class TeacherByUsernameAPIView(APIView):
    permission_classes = [IsAuthenticated, CanUpdateProfile]

    def get(self, request, username):
        teacher = Teacher.objects.get(user__username=username)

        if request.user != teacher.user and not request.user.is_staff:
            return Response({"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
# ============================ Account API ============================#
from django.utils import timezone

class UserLoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Kiểm tra username tồn tại
        try:
            user = User.objects.get(username=username)

        except User.DoesNotExist:
            return Response({'message': 'Username does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        # Kiểm tra password đúng
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'message': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)



        # Kiểm tra is_active
        if not user.is_active:
            return Response({'message': 'Account is inactive'}, status=status.HTTP_403_FORBIDDEN)

        # Đăng nhập thành công
        login(request, user)
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        # Kiểm tra last_login
        if not user.is_superuser:
            if hasattr(user, 'student'):
                if(user.student.isFirstLogin):
                    return Response({
                    'message': 'Please change your password',
                    'access_token': access_token,
                    'refresh_token': str(refresh)})
            if hasattr(user, 'teacher'):
                if(user.teacher.isFirstLogin ):
                    return Response({
                    'message': 'Please change your password',
                    'access_token': access_token,
                    'refresh_token': str(refresh)})

        return Response({
            'message': 'Login successful',
            'access_token': access_token,
            'refresh_token': str(refresh)
        }, status=status.HTTP_200_OK)

class ChangePasswordView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, username):
        user = User.objects.get(username=username)

        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')

        if not old_password or not new_password:
            return Response({"message": "Old password and new password are required."},
                            status=status.HTTP_400_BAD_REQUEST)

        if check_password(old_password, user.password):
            user.set_password(new_password)

            if hasattr(user, 'student'):
                user.student.isFirstLogin = False;
                user.student.save();

            if hasattr(user, 'teacher'):
                user.teacher.isFirstLogin = False;
                user.teacher.save()
            user.save()
            # Cập nhật session authentication hash để tránh đăng xuất sau khi thay đổi mật khẩu
            update_session_auth_hash(request, user)

            return Response({"message": "Password changed successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Old password is incorrect."}, status=status.HTTP_400_BAD_REQUEST)


class ListUserActiveClassroomsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if user.is_superuser:  # Nếu là admin
            classrooms = Classroom.objects.filter(active_status__in = [True])
        else:
            try:
                teacher = Teacher.objects.get(user=user)
                classrooms = teacher.class_join.filter(active_status__in = [True])
            except Teacher.DoesNotExist:
                try:
                    student = Student.objects.get(user=user)
                    classrooms = student.class_join.filter(active_status__in = [True])
                except Student.DoesNotExist:
                    return Response({"message": "User is not a teacher or student."}, status=status.HTTP_403_FORBIDDEN)

        serialized_classrooms = ClassroomSerializer(classrooms, many=True)
        return Response(serialized_classrooms.data)

class ListUserInactiveClassroomsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if user.is_superuser:  # Nếu là admin
            classrooms = Classroom.objects.filter(active_status__in = [False])
        else:
            try:
                teacher = Teacher.objects.get(user=user)
                classrooms = teacher.class_join.filter(active_status__in = [False])
            except Teacher.DoesNotExist:
                try:
                    student = Student.objects.get(user=user)
                    classrooms = student.class_join.filter(active_status__in = [False])
                except Student.DoesNotExist:
                    return Response({"message": "User is not a teacher or student."}, status=status.HTTP_403_FORBIDDEN)

        serialized_classrooms = ClassroomSerializer(classrooms, many=True)
        return Response(serialized_classrooms.data)

class ListUserClassroomsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if user.is_superuser:  # Nếu là admin
            classrooms = Classroom.objects.all()
        else:
            try:
                teacher = Teacher.objects.get(user=user)
                classrooms = teacher.class_join.all()
            except Teacher.DoesNotExist:
                try:
                    student = Student.objects.get(user=user)
                    classrooms = student.class_join.all()
                except Student.DoesNotExist:
                    return Response({"message": "User is not a teacher or student."}, status=status.HTTP_403_FORBIDDEN)

        serialized_classrooms = ClassroomSerializer(classrooms, many=True)
        return Response(serialized_classrooms.data)
