from rest_framework import permissions

from classes.models import Classroom


class CanAddClassroom(permissions.BasePermission):
    def has_permission(self, request, view):
        # Kiểm tra quyền xem danh sách học sinh
        return request.user and  request.user.username.startswith('admin')

class CanUpdateInfoClassroom(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        classroom = obj
        return request.user.is_staff or request.user in classroom.teachers.all()

class IsStudentOrTeacherInClass(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_superuser:
            return True
        if obj.students.filter(user=user).exists() or obj.teachers.filter(user=user).exists():
            return True
        return False